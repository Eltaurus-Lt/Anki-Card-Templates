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

from aqt import mw, gui_hooks
from aqt.qt import QFileDialog, QFileInfo
from aqt.utils import tooltip

from ..utils import files

import json


dic = {}

def _load():
    global dic
    contents = files.col_contents("_deckThumbnails.json") or "{}"
    dic = json.loads(contents)

def _save():
    global dic
    files.col_save(json.dumps(dic), "_deckThumbnails.json")

gui_hooks.main_window_did_init.append(_load)


def set(did):
    global dic
    thumb_filename, _ = QFileDialog.getOpenFileName(
        mw,
        "Select image file",
        "",
        "Image Files (*.png *.jpg *.jpeg *.webp *.gif);;All Files (*.*)"
    )
    if not thumb_filename:
        return
    ext = QFileInfo(thumb_filename).suffix()

    dic[did] = f"_{did}_thumb.{ext}"
    files.col_copy(thumb_filename, dic[did])
    _save()

def remove(did):
    global dic
    files.col_delete(dic[did])
    # dic[did] = None
    del dic[did]
    _save()