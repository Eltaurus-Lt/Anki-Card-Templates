# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2025 Eltaurus
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

addon_path = os.path.dirname(__file__)

def save(path, data):
    file_path = os.path.join(addon_path, "user_files", os.path.normpath(path))

    dir_path = os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)

def location(subfolder, file):
    return "user_files"

def list(subfolder, ext = ""):
    folder_path = os.path.join(addon_path, "user_files", os.path.normpath(subfolder))
    if os.path.exists(folder_path):
        files_user = {os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith(ext)}
    else:
        files_user = set()

    folder_path = os.path.join(addon_path, "stock_files", os.path.normpath(subfolder))
    if os.path.exists(folder_path):
        files_stock = {os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith(ext)}
    else:
        files_stock = set()

    return sorted(files_user | files_stock)