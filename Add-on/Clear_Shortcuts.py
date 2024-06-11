from anki.hooks import wrap
from aqt.reviewer import Reviewer
#from aqt.qt import Qt # slows down deck loading

def removeShortcuts(self, _old):
    keysToRemove = {
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
        # Qt.Key.Key_Enter, Qt.Key.Key_Return, 
        # Qt.Key.Key_Space # does not work?
        }
    actionsToRemove = {
        self.onEnterKey, # Enter
        #self.on_pause_audio, # 5
        #self.on_seek_backward, # 6
        #self.on_seek_forward # 7
        }

    shortcuts = _old(self)
    shortcuts = [key for key in shortcuts if key[0] not in keysToRemove]
    shortcuts = [key for key in shortcuts if key[1] not in actionsToRemove]

    return shortcuts


Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, removeShortcuts, "around")