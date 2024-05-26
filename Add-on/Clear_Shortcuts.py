from anki.hooks import wrap
from aqt.reviewer import Reviewer

def removeShortcuts(self, _old):
    toRemove = {self.onEnterKey}   
    shortcuts = [key for key in _old(self) if key[1] not in toRemove]

    return shortcuts


Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, removeShortcuts, "around")