# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2023-2024 Eltaurus
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

from anki.hooks import wrap
from aqt import mw
from aqt.reviewer import Reviewer
#from aqt.qt import Qt # slows down deck loading

config = mw.addonManager.getConfig(__name__)

def removeShortcuts(self, _old):
    actionAliases = {
        "Enter/Space": self.onEnterKey
        }
    
    # keysToRemove = {
    #     "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    #     # Qt.Key.Key_Enter, Qt.Key.Key_Return, 
    #     # Qt.Key.Key_Space # does not work?
    #     }
    # actionsToRemove = {
    #     self.onEnterKey, # Enter
    #     #self.on_pause_audio, # 5
    #     #self.on_seek_backward, # 6
    #     #self.on_seek_forward # 7
    #     }
    keysToRemove = {key for key in config["reserved keys"] if key not in actionAliases}
    actionsToRemove = {actionAliases[key] for key in config["reserved keys"] if key in actionAliases}

    shortcuts = _old(self)
    shortcuts = [key for key in shortcuts if key[0] not in keysToRemove]
    shortcuts = [key for key in shortcuts if key[1] not in actionsToRemove]

    return shortcuts


Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, removeShortcuts, "around")