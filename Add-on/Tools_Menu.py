import aqt
from . import Dialogs

from aqt.utils import tooltip

import json
    
def NewNoteType():

    dialog = Dialogs.NoteTypeDesigner()
    if not dialog.exec():
        return
    noteType_data = dialog.get_selected_options()

#    json_str = json.dumps(noteType_data)
#	todo: save to file

    tooltip('creation of a new note type initiated')
    return

action = aqt.qt.QAction("New Memrise (Lτ) Note Type", aqt.mw)
action.triggered.connect(NewNoteType)

aqt.mw.form.menuTools.addAction(action)

# tools_list_menu = aqt.qt.QMenu('Memrise (Lτ) Cards', aqt.mw)
# tools_list_menu.addAction(action)
# aqt.mw.form.menuTools.addMenu(tools_list_menu)