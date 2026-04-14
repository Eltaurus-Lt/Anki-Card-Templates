import aqt
from . import Memrise_Cards
from aqt import mw

create_MemriseNT = aqt.qt.QAction("New Memrise (Lτ) Note Type", aqt.mw)
create_MemriseNT.triggered.connect(lambda _: Memrise_Cards.create(mw.col))
aqt.mw.form.menuTools.addAction(create_MemriseNT)

# tools_list_menu = aqt.qt.QMenu('Memrise (Lτ) Cards', aqt.mw)
# tools_list_menu.addAction(action)
# aqt.mw.form.menuTools.addMenu(tools_list_menu)