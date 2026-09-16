# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2023-2026 Eltaurus
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

def dispatch(key_event):
    aqt2js_mapping = {
        " ": (" ", "Space"),
        "16777220": ("Enter", "Enter"), # return
        "16777221": ("Enter", "Enter"), # enter
    }

    keyCombination = [key.lower() for key in str(key_event).split("+")] # for compound shortcuts, e.g. Ctrl+Shift+X
    baseKey = keyCombination[-1]

    # no escaping (for performance), so certain special characters wouldn't work
    dispatch_js = f"""
    (function() {{
        const event = {{
            key: "{aqt2js_mapping.get(baseKey, (None, None))[0] or baseKey}",
            code: "{aqt2js_mapping.get(baseKey, (None, None))[1] or (f"Key{baseKey.upper()}" if baseKey.isalpha() and len(baseKey) == 1 else baseKey)}",
            ctrlKey: {"true" if "ctrl" in keyCombination or "control" in keyCombination else "false"},
            shiftKey: {"true" if "shift" in keyCombination else "false"},
            altKey: {"true" if "alt" in keyCombination else "false"},
            metaKey: {"true" if "meta" in keyCombination or "cmd" in keyCombination or "win" in keyCombination else "false"},
            bubbles: true,
            cancelable: true
        }};
        
        document.dispatchEvent(new KeyboardEvent('keydown', event));
        // document.dispatchEvent(new KeyboardEvent('keyup', event));
    }})();
    """

    mw.reviewer.web.eval(dispatch_js)


def keywrap(key, state: None):
    def conditionedCallback():
        if (
            mw.reviewer and
            (not state or mw.reviewer.state == state) and
            mw.reviewer.card and
            "(Lτ)" in mw.reviewer.card.model()["name"]
        ):
            dispatch(key[0]) # pass key event to webview
        else:
            key[1]() # trigger stock anki callback

    return (key[0], conditionedCallback)

def passShortcuts(self, _old):
    shortcuts = _old(self)
    shortcuts = [keywrap(key, "question") if (isinstance(key[0], str) and key[0] in "1234567890") else key for key in shortcuts]
    shortcuts = [keywrap(key, "answer") if key[1] == self.onEnterKey else key for key in shortcuts]
    return shortcuts

Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, passShortcuts, "around")
