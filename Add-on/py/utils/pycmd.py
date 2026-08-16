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

import inspect

from aqt import gui_hooks

# # todo: 
# bridge(key: str, value)
# return value to js (only test?)

def bridge(pycmds, restrict_to = None):
    def handler(handled, cmd, context):
        def handle(cmd, pycmds):
            for prefix, pycmd in pycmds.items():
                if not cmd.startswith(prefix):
                    continue
                if isinstance(pycmd, dict) and len(cmd) > len(prefix) + 2: # 2 = len of the "::" separator
                    return handle(cmd[len(prefix)+2:], pycmd)
                elif callable(pycmd):
                    Nargs = len(inspect.signature(pycmd).parameters)
                    if Nargs == 0 and prefix == cmd:
                        return (True, pycmd())
                    elif Nargs == 1 and len(cmd) > len(prefix) + 2: 
                        return (True, pycmd(cmd[len(prefix)+2:]))
                    elif Nargs > 1 and len(cmd) > len(prefix) + 2:
                        return (True, pycmd(*[arg.strip() for arg in cmd[len(prefix)+2:].split(",")]))

            return handled

        if restrict_to and not isinstance(context, restrict_to):
            return handled

        return handle(cmd, pycmds)

    gui_hooks.webview_did_receive_js_message.append(handler)