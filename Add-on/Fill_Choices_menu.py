# todo: undo group
from . import Dialogs
from aqt import mw, gui_hooks
from aqt.qt import *
from aqt.utils import tooltip


def fill_choices(browser):
    notes = [mw.col.get_note(note_id) for note_id in browser.selected_notes()]

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
            all_choices.add(note[source_field])

    # Filling choices field on each note
    counter = 0
    for note in notes:
        if choices_field not in note.keys():
            continue
        choices_filtered = {choice for choice in all_choices if (source_field not in note.keys() or choice != note[source_field])}

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