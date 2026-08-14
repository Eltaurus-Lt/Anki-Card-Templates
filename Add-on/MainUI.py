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

import aqt
from . import NoteTypes
from .NoteTypes import NoteTypeManager

# # todo:
# add separator to tool menu

# File Menu

import_Memrise = aqt.qt.QAction("Import Memrise Courses...", aqt.mw)
import_Memrise.triggered.connect(NoteTypes.Memrise.Import)

menu = aqt.mw.form.menuCol
current_actions = menu.actions()
insert_index = None
for i, act in enumerate(current_actions):
	if "Import" in act.text():
		insert_index = i + 1
		break
if insert_index is not None:
	menu.insertAction(current_actions[insert_index], import_Memrise)
else:
	menu.addAction(import_Memrise)



# Tools Menu

new_MemriseNT = aqt.qt.QAction("New Memrise (Lτ) Note Type", aqt.mw)
new_MemriseNT.triggered.connect(NoteTypes.Memrise.Setup)
aqt.mw.form.menuTools.addAction(new_MemriseNT)

# tools_list_menu = aqt.qt.QMenu('Tau Cards', aqt.mw)
# tools_list_menu.addAction(action)
# aqt.mw.form.menuTools.addMenu(tools_list_menu)
