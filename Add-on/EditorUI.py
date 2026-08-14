# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2025-2026 Eltaurus
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

from anki.hooks import addHook
from aqt import gui_hooks
from aqt.qt import *
from .py.utils import files
from .py.Editor import Alts, FillChoices

# # todo:
# convert buttons to new hooks

def setupEditorButtonsFilter(buttons, editor):
    buttons.insert(0,
        editor.addButton(
            files.icon("alts.svg"),
            'alts',
            Alts.format,
            tip = "Format as an alternative (Alt+A)",
            keys="Alt+A"
        )
    )
    buttons.insert(1,
        editor.addButton(
            files.icon("alts-erase.svg"),
            'erase alts',
            Alts.erase,
            tip = "Erase alternative formatting (Alt+X)",
            keys="Alt+X"
        )
    )
    return buttons


def choices_context_menu(browser):
    menuC = browser.form.menu_Cards
    actionC = menuC.addAction("Fill Choices")
    qconnect(actionC.triggered, lambda: FillChoices.Setup(browser))

    menuN = browser.form.menu_Notes
    actionN = menuN.addAction("Fill Choices")
    qconnect(actionN.triggered, lambda: FillChoices.Setup(browser))


addHook("setupEditorButtons", setupEditorButtonsFilter)
gui_hooks.browser_menus_did_init.append(choices_context_menu)