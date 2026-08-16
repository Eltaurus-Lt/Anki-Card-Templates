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

from ..utils import pycmd

pycmd.bridge({
    "action": {
        "card": {
            "bury": mw.reviewer.onBuryCard,
            "suspend": mw.reviewer.onSuspendCard,
        },
        "note": {
            "bury": mw.reviewer.onBuryNote,
            "suspend": mw.reviewer.onSuspend, # (sic!)
        },
        "flag": lambda _: mw.reviewer.setFlag(int(_)) if _.isdigit() else None,
        "undo": mw.onUndo,
        "voice": {
            "record": mw.reviewer.onRecordVoice,
            "replay": mw.reviewer.onReplayRecorded,
        },

        # legacy
        "bury_card": mw.reviewer.onBuryCard,
        "suspend_card": mw.reviewer.onSuspendCard,
        "bury_note": mw.reviewer.onBuryNote,
        "suspend_note": mw.reviewer.onSuspend,
        "voice_record": mw.reviewer.onRecordVoice,
        "voice_replay": mw.reviewer.onReplayRecorded,
    },
}, Reviewer)
