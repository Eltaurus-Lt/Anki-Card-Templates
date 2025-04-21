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

import os, json, re
from anki.hooks import addHook
from aqt import mw
from aqt.utils import tooltip
from . import console

addon_path = os.path.dirname(__file__)

def alts_format_legacy(editor):
    selection = editor.web.selectedText()
    if selection:
        alt_section = '<span part="alt">' + selection + '</span>' # does not work when selection ends at a closnig tag + part gets immediately cleared in 25.02.1+
        editor.web.eval(f"document.execCommand('insertHTML', false, {repr(alt_section)});")


def count_brs(html):
    match = re.search(r'(<br\s*/?>)+\s*$', html)
    if match:
        return match.group(0).count('<br')
    return 0


def alts_format(editor):
    current_field = editor.currentField
    if current_field is None:
        tooltip('No field selected')
        return
    current_note = editor.note

    count_before = count_brs(current_note.fields[current_field])

    js_code = """
        (function() {
            try {    
                const activeElement = document.activeElement;
                const shadowRoot = activeElement.shadowRoot;
                const field = shadowRoot.querySelector('[contenteditable="true"]');
                // const fieldContent0 = field.innerHTML;

                const selection = shadowRoot.getSelection();
                console.log(selection);
                if (selection.rangeCount > 0) {
                    const range = selection.getRangeAt(0);
                    const altDiv = document.createElement('div');
                    altDiv.setAttribute("part", "alt");
                    const contents = range.extractContents();
                    range.insertNode(altDiv);

                    if (contents.hasChildNodes()) {
                        altDiv.appendChild(contents);
                    } else {
                        altDiv.appendChild(document.createElement("br"));
                    }

                    const newrange = document.createRange();
                    newrange.setStart(altDiv, altDiv.childNodes.length);
                    newrange.collapse(true);
                    selection.removeAllRanges();
                    selection.addRange(newrange);
                }

                const fieldContent = field.innerHTML;

                return JSON.stringify({
                    fieldContent: fieldContent
                });
            } catch (error) {
                return JSON.stringify({ error: error.message });
            }
        })();
    """

    def br_cleanup(): # remove stray <br>s inserted by Anki editor
        count_after = count_brs(current_note.fields[current_field])
        count_diff = count_after - count_before

        # tooltip(f"{count_before} -> {count_after}")

        if (count_diff > 0):
            current_note.fields[current_field] = current_note.fields[current_field][:-4 * count_diff]
            mw.col.update_note(current_note)
            editor.loadNoteKeepingFocus()


    def callback(js_result):
        try:
            result = json.loads(js_result)
            if result.get("error"):
                console.log(result["error"], editor)
                if result["error"] == "Cannot read properties of null (reading 'querySelector')":
                    tooltip("formatted field content should be selected instead of html code")
                return

            editor.saveNow(br_cleanup)
                

        except json.JSONDecodeError:
            tooltip("An error occurred while processing the selection!")

    editor.web.evalWithCallback(js_code, callback)

def alts_erase(editor):
    current_field = editor.currentField
    if current_field is None:
        tooltip('No field selected')
        return

    js_code = """
        (function() {
            try {    
                const activeElement = document.activeElement;
                const shadowRoot = activeElement.shadowRoot;
                const field = shadowRoot.querySelector('[contenteditable="true"]');
                // const fieldContent0 = field.innerHTML;

                const altDivs = field.querySelectorAll('div[part="alt"]');

                altDivs.forEach(altDiv => {
                    const parent = altDiv.parentNode;

                    while (altDiv.firstChild) {
                        parent.insertBefore(altDiv.firstChild, altDiv);
                    }

                    parent.removeChild(altDiv);
                });

                const fieldContent = field.innerHTML;

                return JSON.stringify({
                    fieldContent: fieldContent
                });
            } catch (error) {
                return JSON.stringify({ error: error.message });
            }
        })();
    """

    def callback(js_result):
        try:
            result = json.loads(js_result)
            if result.get("error"):
                console.log(result["error"], editor)
                if result["error"] == "Cannot read properties of null (reading 'querySelector')":
                    tooltip("formatted field content should be selected instead of html code")
                return

        except json.JSONDecodeError:
            tooltip("An error occurred while processing the selection!")

    editor.web.evalWithCallback(js_code, callback)

def setupEditorButtonsFilter(buttons, editor):
    buttons.insert(0,
        editor.addButton(
            os.path.join(addon_path, "icons", "alts.svg"),
            'alts',
            alts_format,
            tip = "Format as an alternative (Alt+A)",
            keys="Alt+A"
        )
    )
    buttons.insert(1,
        editor.addButton(
            os.path.join(addon_path, "icons", "alts-erase.svg"),
            'erase alts',
            alts_erase,
            tip = "Erase alternative formatting (Alt+X)",
            keys="Alt+X"
        )
    )

    return buttons

addHook("setupEditorButtons", setupEditorButtonsFilter)