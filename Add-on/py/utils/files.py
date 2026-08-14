# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2025-2026 Eltaurus
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


import os
from aqt import mw
# from . import console

addons_folder = mw.addonManager.addonsFolder()
addon_name = mw.addonManager.addonFromModule(__name__)
addon_root = os.path.join(addons_folder, addon_name)
# addon_url = 

# todo: remove unnecessary normpaths

def _path(path, root = addon_root):
    if os.path.isfile(root):
        root = os.path.dirname(os.path.abspath(root))

    return os.path.normpath(os.path.join(root, os.path.normpath(path)))

def _user_path(path):
    return os.path.join("user_files", os.path.normpath(path))


def contents(file_path, root = addon_root):
    full_path = _path(file_path, root)
    if not os.path.isfile(full_path):
        return ""

    with open(full_path, 'r', encoding='utf-8') as file:
        return file.read()


def file_list(ext, path, root = addon_root):
    folder_path = _path(path, root)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return {os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith(ext)}
    else:
        return set()

def user_list(ext, path):
    return file_list(ext, _user_path(path))


def user_save(data, path):
    file_path = os.path.join(addon_root, _user_path(path))

    dir_path = os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)


def icon(icon_file):
    return os.path.join(addon_root, "icons", icon_file)