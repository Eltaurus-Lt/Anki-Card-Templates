# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2023-2025 Eltaurus
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

from . import Dialogs
from aqt import mw, gui_hooks
from aqt.qt import *
from aqt.utils import tooltip

from bs4 import BeautifulSoup

def removeAlts(fieldContents):
    if fieldContents.find('alt') == -1:
        return fieldContents

    if fieldContents.find('class') == -1 and fieldContents.find('part') == -1:
        return fieldContents

    soup = BeautifulSoup(fieldContents, "html.parser")

    for element in soup.find_all(attrs={"class": "alt"}):
        element.decompose()

    for element in soup.find_all(attrs={"part": "alt"}):
        element.decompose()

    return str(soup)


def fill_choices(browser):
    notes = [mw.col.get_note(note_id) for note_id in browser.selected_notes()]

    if len(notes) < 2:
        tooltip('at least two notes have to be selected')
        return

    # Defining a set of all fields present in the selected notes
    unique_fields = []
    added = set()
    for note in notes:
        for field in note.keys():
            if not (field in added or added.add(field)):
                unique_fields.append(field)

    # Settings Dialog
    dialog = Dialogs.FillChoices(unique_fields)
    if not dialog.exec():
        return
    source_field, choices_field, append = dialog.get_selected_options()

    # Gathering all potential choice options
    all_choices = set()
    for note in notes:
        if source_field in note.keys():
            all_choices.add(removeAlts(note[source_field]))

    # Filling choices field on each note
    counter = 0
    for note in notes:
        if choices_field not in note.keys():
            continue
        choices_filtered = {choice for choice in all_choices if (source_field not in note.keys() or choice != removeAlts(note[source_field]))}

        if append and note[choices_field]:
            choices_filtered.update([choice.strip() for choice in note[choices_field].split("|")])

        note[choices_field] = " | ".join([choice for choice in choices_filtered if choice])
        mw.col.update_note(note)
        counter += 1

    tooltip(f'Choices filled for {counter} notes')
    


def choices_context_menu(browser):
    menuC = browser.form.menu_Cards
    actionC = menuC.addAction("Fill Choices")
    qconnect(actionC.triggered, lambda: fill_choices(browser))

    menuN = browser.form.menu_Notes
    actionN = menuN.addAction("Fill Choices")
    qconnect(actionN.triggered, lambda: fill_choices(browser))


gui_hooks.browser_menus_did_init.append(choices_context_menu)