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

import json
from ...py.utils import files
from ...py.utils import indexOf

def version():
    return "5.2"

def list_themes(include_default = True):
    stock_themes = files.file_list(".css", "Themes", __file__)
    user_themes = files.user_list(".css", "Memrise Themes")
    return (["ー"] if include_default else [])  + sorted(stock_themes | user_themes)

def default_theme(theme_list):
    return indexOf(theme_list, "Memrise", indexOf(theme_list, "Anki", 1))

def list_presets():
    preset_list = sorted(files.user_list(".json", "Memrise Presets"))
    if "default" in preset_list:
        preset_list.pop(preset_list.index("default"))
    return ["default"] + preset_list

def load_theme(theme):
    return (
        files.contents(f"user_files/Memrise Themes/{theme}.css")
        or files.contents(f"Themes/{theme}.css", __file__) # stock
    )

def load_preset(preset):
    preset_json = (
        files.contents(f"user_files/Memrise Presets/{preset}.json")
        or files.contents(f"{preset}.json", __file__) # default
    )
    if preset_json:
        return json.loads(preset_json)

def save_preset(name, data):
    preset_json = json.dumps(data, ensure_ascii=False, indent=4)
    files.user_save(preset_json, f"Memrise Presets/{name}.json")