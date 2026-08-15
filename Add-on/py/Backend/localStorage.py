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

from aqt import gui_hooks
from aqt.utils import tooltip

from ..utils import files, inject

def inject_js(web_content, context) -> None:
    if localStorage := files.col_contents("_localStorage.json"):
        inject.json_content(localStorage, web_content, tag_id="localStorage-old")
        inject.js_content("localStorage.load.js", web_content)
    inject.js_content("localStorage.save.js", web_content) # listener

def save_bridge(handled, cmd, context):
    prefix = "save_localStorage::"
    if not cmd.startswith(prefix):
        return handled

    if e := files.col_save(cmd[len(prefix):], "_localStorage.json"):
        tooltip(f"localStorage save error: {e}")
        
    return (True, None)

gui_hooks.webview_will_set_content.append(inject_js)
gui_hooks.webview_did_receive_js_message.append(save_bridge)
