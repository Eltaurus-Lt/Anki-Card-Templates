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


from anki.models import ModelManager
from aqt.utils import tr, getText
from aqt import mw
from ...py.utils import files as file
from ..make_utils import wrapScript


def placeJS(js_file):
    return wrapScript(file.contents("Template/"+js_file+".js", __file__))



def Assemble(name):
    mm = mw.col.models
    noteType = mm.new(name)

    # Fields
    mm.addField(noteType, mm.newField("Front"))
    mm.addField(noteType, mm.newField("Back"))

    # Card Type
    cardType = mm.newTemplate("Card 1")
    cardType["qfmt"] = (
                        '<data id="expans">{{Back}}</data>\n'
                        '\n'
                        '{{Front}}\n'
                        '\n'
                        '<input id="typeans" type="text" inputmode="text" autocorrect="off" autocomplete="off" autocapitalize="off" spellcheck="false">\n'
                        f"{placeJS('Cross-platform Typing (front)')}"
                        f"{placeJS('AnkiWeb audio')}"
                        )
    cardType["afmt"] = (
                        '{{Front}}\n'
                        '\n'
                        '<hr id=answer>\n'
                        '\n'
                        '<input id="typeans">\n'
                        f"{placeJS('Cross-platform Typing (back)')}"
                        f"{placeJS('AnkiWeb audio')}"
                       )
    noteType["css"] = (
                        f'{file.contents("Template/common.css", __file__)}\n'
                        '\n'
                        f'{file.contents("Template/style resets.css", __file__)}\n'
                        '\n'
                        '\n'
                        '\n'
                        '/* card styling */\n' 
                        '\n'
                        '.card {\n'
                        '    font-family: arial;\n'
                        '    font-size: 20px;\n'
                        '    line-height: 1.5;\n'
                        '    text-align: center;\n'
                        '    color: black;\n'
                        '    background-color: white;\n'
                        '}'
                       )
    mm.addTemplate(noteType, cardType)

    # Add to the collection
    mm.add(noteType)
    mm.save(noteType)

    return noteType


def Setup(*args):
    noteTypeName, ok = getText(tr.actions_name(), default = "Basic (Lτ)")

    if ok:
        return Assemble(noteTypeName)
    return mw.col.models.current() 