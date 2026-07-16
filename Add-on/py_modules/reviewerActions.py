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

from aqt import gui_hooks, mw
from aqt.reviewer import Reviewer

def actions_listener(handled, cmd, context):
    if not isinstance(context, Reviewer):
        return handled

    # 1. Bury and Susupend
    if cmd == "action::bury_card":
        mw.reviewer.onBuryCard()
        return (True, None)
    if cmd == "action::bury_note":
        mw.reviewer.onBuryNote()
        return (True, None)
    if cmd == "action::suspend_card":
        mw.reviewer.onSuspendCard()
        return (True, None)
    if cmd == "action::suspend_note":
        mw.reviewer.onSuspend() # (sic!)
        return (True, None)

    # 2. Flag
    prefix = "action::flag::"
    if cmd.startswith(prefix):
        try:
            flag_i = int(cmd[len(prefix)])
            mw.reviewer.setFlag(flag_i)
        except ValueError:
            pass
        return (True, None)

    # 3. Undo
    if cmd == "action::undo":
        mw.onUndo()
        return (True, None)

    # 4. Voice actions
    if cmd == "action::voice_record":
        mw.reviewer.onRecordVoice()
        return (True, None)
    if cmd == "action::voice_replay":
        mw.reviewer.onReplayRecorded()
        return (True, None)
        
    return handled

gui_hooks.webview_did_receive_js_message.append(actions_listener)
