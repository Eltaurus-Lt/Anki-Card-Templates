import aqt
from . import Memrise_Cards
from . import Memrise_Import

create_MemriseNT = aqt.qt.QAction("New Memrise (Lτ) Note Type", aqt.mw)
create_MemriseNT.triggered.connect(Memrise_Cards.create)
aqt.mw.form.menuTools.addAction(create_MemriseNT)

# tools_list_menu = aqt.qt.QMenu('Memrise (Lτ) Cards', aqt.mw)
# tools_list_menu.addAction(action)
# aqt.mw.form.menuTools.addMenu(tools_list_menu)


import_Memrise = aqt.qt.QAction("Import from Memrise...", aqt.mw)
import_Memrise.triggered.connect(Memrise_Import.import_courses)

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