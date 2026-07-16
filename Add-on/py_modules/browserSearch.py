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

from aqt import dialogs, gui_hooks, mw


def search_listener(handled, cmd, context):
    prefix = "action::search:"
    if not cmd.startswith(prefix):
        return handled

    search_query = cmd[len(prefix):]
    browser = dialogs.open("Browser", mw)
    browser.form.searchEdit.lineEdit().setText(search_query)
    browser.onSearchActivated()
    return (True, None)


gui_hooks.webview_did_receive_js_message.append(search_listener)
