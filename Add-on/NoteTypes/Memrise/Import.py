# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2026 Eltaurus
# Contact: 
#     Email: Eltaurus@inbox.lt
#     GitHub: github.com/Eltaurus-Lt
#     Anki Forums: forums.ankiweb.net/u/Eltaurus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os, re, csv, json

from aqt import mw
from aqt.utils import tooltip

from ...py.Dialogs import QBatchDialog
from .Dialogs.Import import MemriseImportSettings

# todo
# # D root bug
# # settings dialog
# # # selectable rows for batch setup (fix height)
# # # renamable NTs
# # # *advanced
### move theme inside the table ( existing NT - deactivate; new NT - change for all courses with same NT when changed / autochange when NT is changed to new and used by other course)

# learnable id == in different directions??

# # import
# # # merge notes
# # # media (renames table)
# # # create decks
# # # create NTs
# # # meta
# # # tags
# # # revlog
# # choices
# # # fill
# # # Audio Q
# # # convert img and audio 
# # !progress bar
# # # ... todos
# # test
# # # (old) courses with no headers
# # # saving/renaming presets
# # # user themes


import_folder = os.path.expanduser("~/Downloads")

def selectCourses():
    def courseScan(root_path):
        def shortTab(csv_filename): # short 
            match = re.match(r"^(.+)\[(\d+)\](?:_\((?:~?\d+|\d+ of \d+)\))?\.csv$", csv_filename)
            return (match.group(1).strip(), match.group(2)) if match else False

        def fullTab(short_tab, full_path):
            global import_folder

            rel_path = os.path.relpath(full_path, import_folder).split(os.sep)

            deck_tree = rel_path[:-1]

            if len(deck_tree) > 0 and deck_tree[-1].startswith(short_tab[0]):
                deck_tree.pop()

            return {
                    "name": short_tab[0],
                    "id": short_tab[1],
                    "deck tree": deck_tree,
                    "csv path": full_path
                    }

        if os.path.isdir(root_path):
            course_tabs = []
            for root, _, files in os.walk(root_path):
                for f in files:
                    if short_tab := shortTab(f):
                        course_tabs.append((short_tab, os.path.join(root, f)))
            return [fullTab(*course_tab) for course_tab in course_tabs]
        elif os.path.isfile(root_path) and (short_tab := shortTab(os.path.basename(root_path))):
            return [fullTab(short_tab, root_path)]

        return []

    ## File Selection Dialog
    global import_folder
    file_dialog = QBatchDialog(
        caption = "Select course .csv files, course folders, or a parent folder with multiple courses",
        directory = import_folder,
        filter = "CSV Files (*.csv);;All Files (*)"
    )

    selected_paths = None
    if file_dialog.exec():
        selected_paths = file_dialog.selectedFiles()
    if selected_paths is None:
        # tooltip("No files selected")
        return

    courses = [course for path in selected_paths for course in courseScan(path)]

    if not courses:
       tooltip("No courses found in the selection")
       return

    return courses


def selectOptions(courses):
    if not courses: return

    ## Import Options Dialog
    dialog = MemriseImportSettings(courses)
    if not dialog.exec():
        return
    course_options = dialog.course_options()
    import_options = dialog.import_options()

    # mw.reviewer.web.eval(f'console.log(`{str(course_options)}`)')
    # mw.reviewer.web.eval(f'console.log(`{str(import_options)}`)')

    if not course_options:
        tooltip("No courses selected for import")

    return course_options, import_options


def groupByNoteTypes(course_options):
    noteTypes = {}
    for course in course_options:
        if course["Note Type"] in noteTypes:
            noteTypes[course["Note Type"]]["courses"].append(course)
        else:
            noteTypes[course["Note Type"]] = {
                # assign unique names to auto
                "name": course["name"] if (course["NT_isNew"] and course["Note Type"].startswith("(auto ") and course["Note Type"].endswith(")") ) else course["Note Type"], 
                "is_new": course["NT_isNew"],
                "courses": [course]
            }
    return noteTypes


def parseCourse(course, import_options):

    learn_col = -1
    def_col = -1
    tags_col = -1
    prog_col = -1
    meta_col = -1
    columns = []

    cards = []
    card_fields = []
    card_types = []

    with open(course["csv path"], newline="", encoding="utf-8") as csv_file:
        for row in csv.reader(csv_file):

            # file headers
            row0 = row[0][1:] if row[0].startswith("\ufeff") else row[0] # removing BOM
            if row0.startswith("#"):
                if row0.startswith("#tags column:"):
                    tags_col = int(row0[len("#tags column:"):]) - 1
                elif row0.startswith("#columns:"):
                    for i in range(len(row)):
                        # column headers
                        header = row[i] if i > 0 else row0[len("#columns:"):]
                        columns.append(header)
                        if header == "Learnable":
                            learn_col = i
                        elif header == "Definition":
                            def_col = i
                        elif header == "Learnable meta":
                            meta_col = i
                        elif header == "Progress":
                            prog_col = i
                        elif header == "Level tags" and tags_col < 0:
                            tags_col = i
                continue

            # cards
            card = {"Fields": {}, "Choices": {}, "Direction": "Definition → Learnable", "Level": False, "Tags": ""}

            if prog_col >= 0 and row[prog_col] and row[prog_col] != "new":
                try:
                    card["Progress"] = json.loads(row[prog_col])
                except:
                    tooltip(f"{course["id"]}: invalid progress json")

            meta = False
            if meta_col >= 0 and row[meta_col]:
                try:
                    meta = json.loads(row[meta_col])
                    if not meta or not meta["learnable"] or not meta["definition"]:
                        meta = False
                    if meta:
                        card["Direction"] = f"{meta["definition"]} → {meta["learnable"]}"
                        if temp := meta["choices"]:
                            card["Choices"][meta["learnable"]] = set(temp)
                        if temp := meta["reverse choices"]:
                            card["Choices"][meta["definition"]] = set(temp)
                except:
                    tooltip("invalid learnable meta json")
            if card["Direction"] not in card_types:
                card_types.append(card["Direction"])
            card["History"] = {}

            for i in range(len(row)):
                if columns and i < len(columns):
                    field = columns[i]
                elif i == 0:
                    field = "Learnable"
                elif i == 1:
                    field = "Definition"
                else:
                    field = f"Extra {i - 1}"

                if i == learn_col:
                    if meta:
                        field = meta["learnable"]
                elif i == def_col:
                    if meta:
                        field = meta["definition"]
                elif i == tags_col:
                    card["Tags"] = row[i]
                    card["Level"] = row[i].split("::")[-1].replace("_", " ")
                    continue
                elif i == prog_col or i == meta_col:
                    continue
                
                if field not in card_fields:
                    card_fields.append(field)
                if row[i]:
                    card["Fields"][field] = row[i]

            cards.append(card)

    return cards, card_fields, card_types


def copyMedia(course):
    rename_dict = {}
    # todo
    return rename_dict

def mediaRename(note, rename_dict):
    # todo
    def renameField(field_contents):
        return field_contents
    return note

def mergeIntoNotes(cards):
    notes = []
    # todo
    for card in cards:
        note = {
            "Fields": card["Fields"],
            "Choices": card["Choices"],
            "Tags": card["Tags"],
            "Cards": {
                card["Direction"]: {
                    "Level": card.get("Level"),
                    "History": card["History"]
                }
            }
        }
        notes.append(note)

    return notes



def Import(*args):

    # courses = [...{ name (str), id (int_str), deck tree [...folder (str)], csv path (str) } ]
    courses = selectCourses()

    # course_options = [...{ name (str), id (int_str), deck tree [...folder (str)], csv path (str), Note Type (str), NT_isNew (✓) } ]
    # import_options = { theme (str), import::meta (✓), import::media (✓), import::revlog (✓), tests::audio (✓), tests::typing (✓), tests::multichoice (✓), tests::tapping (✓), advanced::... (todo) }
    course_options, import_options = selectOptions(courses)
    if not course_options or not import_options: return

    # noteType_courses = { ...noteType: { name (str), is_new (✓), courses: [...course] } }
    noteType_courses = groupByNoteTypes(course_options)

    for noteType in noteType_courses.values():
        fields = []
        notes = []
        for course in noteType["courses"]:
            # cards = [...{ Fields: { field: content (str) }, Choices: {...field: [...choices (str)] }, Direction (str), Level (str), Tags (str), History {mem} } ]
            cards, card_fields, card_types = parseCourse(course, import_options)
            
            rename_dict = copyMedia(course)
            # create decks
            # copy deck meta
            ... #todo

            # notes = [...{ Fields: { ...field: content (str) }, Choices: {...field: [...choices (str)] }, Cards: { ...Direction: { Level (str), History {mem} } }, Tags (str) } ]
            card_notes = mergeIntoNotes(cards)

            notes += [mediaRename(note, rename_dict) for note in card_notes]
            fields += [field for field in card_fields if field not in fields]

        # todo
        flag_fields = []
        # create note type
        if noteType["is_new"]:
            ... #todo

        for note in notes:
            # create note (with flags)
            ... # todo

            # fill choices
            ... # todo

            # move cards into decks
            # if levelsubdecks and not level_deck:
            #   create deck
            ... # todo

            # write history
            ... # todo
