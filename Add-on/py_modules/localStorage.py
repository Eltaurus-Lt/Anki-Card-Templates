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

from aqt.utils import tooltip

from aqt import mw, gui_hooks
import os, json

mw.addonManager.setWebExports(__name__, r"js/.*\.js$")
# addons_folder = mw.addonManager.addonsFolder()
addon_name = mw.addonManager.addonFromModule(__name__)

def storage_dump_file():
    if not mw.col or not mw.col.media: # not available during app startup
        return None
    return os.path.join(mw.col.media.dir(), "_localStorage.json")

def js_url(filename):
    return f"/_addons/{addon_name}/js/{filename}"

def inject_js(web_content, context) -> None:
    dump_path = storage_dump_file()
    if not dump_path:
        return

    localStorage = ""
    try:
        with open(dump_path, "r", encoding="utf-8") as f:
            localStorage =  f.read()
    except:
        pass

    if localStorage:
        web_content.head += f"<script type='application/json' id='localStorage-old'>{localStorage}</script>"
        web_content.js.append(js_url("localStorage.load.js"))
    web_content.js.append(js_url("localStorage.save.js")) # creates a listener

def save_listener(handled, cmd, context):
    prefix = "save_localStorage::"
    if not cmd.startswith(prefix):
        return handled

    try:
        localStorage_json = cmd[len(prefix):]
        with open(storage_dump_file(), "w", encoding="utf-8") as f:
            f.write(localStorage_json)
    except Exception as e:
        tooltip(f"localStorage save error: {e}")
        
    return (True, None)

gui_hooks.webview_will_set_content.append(inject_js)
gui_hooks.webview_did_receive_js_message.append(save_listener)
