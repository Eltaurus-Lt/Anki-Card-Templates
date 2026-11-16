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
from aqt.qt import QFileInfo

from ...py.Dialogs import QBatchDialog
from ...py.Backend import Thumbnails
from ...py.utils import files
from .Dialogs.Import import MemriseImportSettings
from . import Create

from aqt.utils import tooltip
from ...py.utils import console

# todo
# # fix root folder determination
# # # D root bug
# # thumbnail refresh without reset
# # # expand all non-level decks
# # author in meta from course name as fallback
# # max deckname length (overview screen)

# # import
# # # direction flag fields
# # # Audio Q
# # # reverse Q

# # choices
# # # import
# # # fill
# # # convert img and audio 


# # import
# # # revlog
# # # # preexisting NTs
# # # merge notes (learnable id == in different directions??)

# # # media renames
# # autofill onscreen keyboard
# # fsrs by default (+adv setting) | import difficulty

# # settings dialog
# # # selectable rows for batch setup (fix height)
# # # renamable NTs
# # # *advanced
### move theme inside the table ( existing NT - deactivate; new NT - change for all courses with same NT when changed / autochange when NT is changed to new and used by other course)
# # !progress bar

# # test
# # # partially deleted meta (author fallback)
# # # (old) courses with no headers
# # # saving/renaming presets
# # # user themes
# # # selected folders have no courses
# # # option to not import/hide on the back Learnable ID
# # # ... todos
# # # mw.reset()


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
            course_folder = None

            if len(deck_tree) > 0 and deck_tree[-1].startswith(short_tab[0]):
                course_folder = os.path.join(import_folder, *deck_tree)
                deck_tree.pop()

            return {
                    "name": short_tab[0],
                    "id": short_tab[1],
                    "deck_tree": deck_tree,
                    "folder": course_folder,
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
    unnamed = 0

    cards = []
    course_fields = []
    course_directions = []

    with open(course["csv path"], newline="", encoding="utf-8") as csv_file:
        for row in csv.reader(csv_file):
            # empty line
            if not row:
                continue

            # file headers
            cell0 = row[0][1:] if row[0].startswith("\ufeff") else row[0] # removing BOM
            if cell0.startswith("#"):
                if cell0.startswith("#tags column:"):
                    tags_col = int(cell0[len("#tags column:"):]) - 1
                elif cell0.startswith("#columns:"):
                    for i in range(len(row)):
                        # column headers
                        header = row[i] if i > 0 else cell0[len("#columns:"):]
                        if not header.strip():
                            header = f"unnamed_field_{unnamed}"
                            unnamed += 1
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
            if card["Direction"] not in course_directions:
                course_directions.append(card["Direction"])
            card["History"] = {}

            for i in range(len(row)):
                if columns and i < len(columns):
                    field = columns[i]
                elif i == 0:
                    field = "Learnable"
                    #todo: replace from meta when no columns
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
                
                if field not in course_fields:
                    course_fields.append(field)
                if row[i]:
                    card["Fields"][field] = row[i]

            cards.append(card)

    return cards, course_fields, course_directions


def copyMedia(media_folder):
    rename_dict = {}
    if not media_folder:
        return rename_dict

    for media_file in os.listdir(media_folder):
        files.col_copy(os.path.join(media_folder, media_file), media_file)
    
    return rename_dict

def mediaRename(note, rename_dict):
    # todo
    def renameField(field_contents):
        return field_contents
    return note

def mergeIntoNotes(cards, course_deck):
    notes = []
    # todo
    for card in cards:
        note = {
            "Fields": card["Fields"],
            "Choices": card["Choices"],
            "Tags": card["Tags"],
            "Deck": course_deck,
            "Cards": {
                card["Direction"]: {
                    "Level": card.get("Level"),
                    "History": card["History"]
                }
            }
        }
        notes.append(note)

    return notes


def getMeta(course):
    meta = {}

    parent_folder = os.path.dirname(course["csv path"])
    for entry in os.listdir(parent_folder):
        full_path = os.path.join(parent_folder, entry)
        if os.path.isdir(full_path) and entry.startswith(f"{course["name"]} [{course["id"]}]_media"):
            meta["media folder"] = full_path

    if not course["folder"] or not os.path.isfile(meta_path := os.path.join(course["folder"], "info.md")):
        # tooltip("no meta")
        return meta

    meta["author"] = None
    meta["description"] = ""
    desc_started = False
    with open(meta_path, newline="", encoding="utf-8") as meta_file:
        for line in meta_file.readlines():
            if line.startswith("# **") and line.endswith("**\n"):
                meta["name"] = line[len("# **"):-len("**\n")]
            if line.startswith("### by"):
                meta["author"] = meta["author"] or line[len("### by"):].strip().strip("_")
            if line.strip() and not line.startswith("#"):
                desc_started = True
            if desc_started:
                meta["description"] += line

    def find_img_file(prefix):
        for file_name in os.listdir(course["folder"]):
            full_path = os.path.join(course["folder"], file_name)
            if not os.path.isfile(full_path):
                continue
            name, ext = os.path.splitext(file_name)
            if ext.lower() not in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff"}:
                continue
            if name.startswith(prefix):
                return full_path

    meta["thumbnail"] = find_img_file(course["name"])
    if meta["author"]:
        meta["ava"] = find_img_file(meta["author"])

    return meta

def formatDescription(meta):
    author_html = ""
    if meta.get("author"):
        if meta.get("ava"):
            author_html += f"<img src='{meta["ava"]}'> "
        author_html += f"<span class='author-name'>{meta["author"]}</span>"
    description = ""
    if author_html:
        description += f"<div class='course-author'><span>by</span> {author_html}</div>"
    if meta.get("description"):
        description += f"<div class='course-description'>{meta["description"]}</div>"
    return description



def completeCardTypeData(card_type_data, input_mode, audio = False):
    return {
        "Name": f"{card_type_data["direction"]} ({input_mode})",
        "Q": card_type_data["Q"],
        "A": card_type_data["A"],
        "in": input_mode,
        "prompt": "Type the correct answer" if input_mode == "Typing" else "Pick the correct answer",
        "Extra": card_type_data["Extra"],
        "Origin": card_type_data["direction"]
    }


def Import(*args):

    # courses = [...{ name (str), id (int_str), deck_tree [str], folder (str), csv path (str) } ]
    courses = selectCourses()

    # course_options = [...{ name (str), id (int_str), deck_tree [str], folder (str), csv path (str), Note Type (str), NT_isNew (✓) } ]
    # import_options = { theme (str), import::meta (✓), import::media (✓), import::revlog (✓), tests::audio (✓), tests::typing (✓), tests::multichoice (✓), tests::tapping (✓), advanced::... (todo) }
    course_options, import_options = selectOptions(courses) or (None, None)
    if not course_options or not import_options: return

    # noteType_courses = { ...noteType: { name (str), is_new (✓), courses: [...course] } }
    noteType_courses = groupByNoteTypes(course_options)

    for noteType in noteType_courses.values():
        fields = []
        notes = []
        directions = []
        for course in noteType["courses"]:
            # cards = [...{ Fields: { field: content (str) }, Choices: {...field: [...choices (str)] }, Direction (str), Level (str), Tags (str), History {mem} } ]
            cards, course_fields, course_directions = parseCourse(course, import_options)

            course_meta = getMeta(course)

            # create decks with descriptions
            full_deck_name = "::".join([*course["deck_tree"], course_meta.get("name") or course["name"]]) # todo: or course["name"]
            did = mw.col.decks.id(full_deck_name) # creates the deck (with parents) if new
            if (deck := mw.col.decks.get(did)):
                if import_options["import::meta"]:
                    if course_meta.get("thumbnail"):
                        Thumbnails.set(did, course_meta["thumbnail"])
                    if course_meta.get("ava"):
                        ava_ext = QFileInfo(course_meta["ava"]).suffix()
                        ava_filename = f"_{course_meta["author"]}_memuser.{ava_ext}"
                        files.col_copy(course_meta["ava"], ava_filename)
                        course_meta["ava"] = ava_filename
                    if description := formatDescription(course_meta):
                        deck["desc"] = description
                        mw.col.decks.save(deck)
            else:
                tooltip(f"error creating course deck [{course["id"]}]")
                continue

            rename_dict = copyMedia(course_meta.get("media folder")) if import_options["import::media"] else {}

            # notes = [...{ Deck (str), Fields: { ...field: content (str) }, Cards: { ...Direction: { Level (str), History {mem} } }, Choices: {...field: [...choices (str)] }, Tags (str) } ]
            card_notes = mergeIntoNotes(cards, full_deck_name)

            notes += [mediaRename(note, rename_dict) for note in card_notes]
            fields += [field for field in course_fields if field not in fields]
            directions += [direction for direction in course_directions if direction not in directions]

        if not fields or not notes or not directions:
            continue

        # setup the note type
        model = None
        card_types = []
        if noteType["is_new"]:
            # create new note type
            field_data = [{
                "Name": field,
                "large": False,
                "back": True,
                "math": False,
                "static": "",
                "random": "",
            } for field in fields]

            for direction in directions:
                Q_field, A_field = direction.split(" → ", 1)
                Extra_field = next((field for field in fields if field not in [Q_field, A_field, "Audio", "Image"]), "ー")
                card_type_data = {
                    "direction": direction,
                    "Q": Q_field,
                    "A": A_field,
                    "Extra": Extra_field
                }

                if import_options["tests::multichoice"]:
                    card_types.append(completeCardTypeData(card_type_data, "Multiple-Choice"))
                if import_options["tests::tapping"]:
                    card_types.append(completeCardTypeData(card_type_data, "Tapping"))
                if import_options["tests::typing"] or (not import_options["tests::tapping"] and not import_options["tests::multichoice"]):
                    card_types.append(completeCardTypeData(card_type_data, "Typing"))

            noteType_setup = {
                "Note Type": noteType["name"],
                "Fields": field_data,
                "Card Types": card_types, 
                "Theme": import_options["theme"]
            }

            model = Create.Assemble(noteType_setup)
        else:
            model = mw.col.models.by_name(noteType["name"])
            # todo: card type origins here
        if not model:
            tooltip(f"error setting up {"new " if noteType["is_new"] else ""}model {noteType["name"]}")
            continue


        for note_data in notes:
            # create note
            note = mw.col.new_note(model)

            for field in model["flds"]:
                if field["name"] in note_data["Fields"]:
                    note[field["name"]] = note_data["Fields"][field["name"]]

            note.add_tag(f"{note_data["Tags"]} Memrise")

            # fill choices
            ... # todo

            course_did = mw.col.decks.id(note_data["Deck"])
            mw.col.add_note(note, course_did)
            

            # move cards to level subdecks
            course_deck = mw.col.decks.get(course_did)
            for card_id in note.card_ids():
                card = mw.col.get_card(card_id)
                card_type = card_types[card.ord]
                level = note_data["Cards"][card_type["Origin"]]["Level"].replace("::", "_")
                level_N, level_name = re.match(r'(\d+)\s*(.*)', level).groups()
                level_did = mw.col.decks.id(f"{full_deck_name}::L{level_N}. {level_name}")
                if level_did is None:
                    continue
                mw.col.set_deck([card_id], level_did)
                level_deck = mw.col.decks.get(level_did)
                if not level_deck["desc"] and course_deck["desc"]:
                    level_deck["desc"] = course_deck["desc"]
                    mw.col.decks.save(level_deck)

            # import history
            if import_options["import::revlog"]:
                ... #todo

    mw.deckBrowser.refresh()
