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

from aqt import gui_hooks, mw
from aqt.webview import WebContent
from aqt.deckbrowser import DeckBrowser
from aqt.overview import Overview
from aqt.editor import Editor
from aqt.reviewer import Reviewer
from aqt.browser.previewer import Previewer
from aqt.clayout import CardLayout
import os, re, json

config = mw.addonManager.getConfig(__name__)
mw.addonManager.setWebExports(__name__, r"css/.*\.css|js/.*\.js|user_files/(.*\.(css|js))$")
addons_folder = mw.addonManager.addonsFolder()
addon_name = mw.addonManager.addonFromModule(__name__)


def general_injector(inj_filename, css_target, js_target):
    inj_type = os.path.splitext(inj_filename)[1].lstrip(".").lower()

    if inj_type == "css":
        target = css_target
    elif inj_type == "js":
        target = js_target
    else:
        return

    if os.path.exists(os.path.join(addons_folder, addon_name, inj_type, inj_filename)):
        target.append(f"/_addons/{addon_name}/{inj_type}/{inj_filename}")
    if os.path.exists(os.path.join(addons_folder, addon_name, "user_files", inj_filename)):
        target.append(f"/_addons/{addon_name}/user_files/{inj_filename}")
        

def window_injector(web_content: WebContent, context: None):
    # passing add-on config
    web_content.head +=f"<setting id='lt-config' data-config='{json.dumps(config)}'></setting>"

    def inject(inj_filename):
        return general_injector(inj_filename, web_content.css, web_content.js)

    inject("common_styles.css")
    inject("common_scripts.js")

    if isinstance(context, (DeckBrowser, Overview)):
        inject("deck_styles.css")
        inject("deck_scripts.js")

    if isinstance(context, Editor):
        inject("editor_styles.css")
        inject("editor_scripts.js")

    if isinstance(context, (Reviewer, Previewer, CardLayout)):
        inject("reviewer_styles.css")
        inject("reviewer_scripts.js")


def to_id(string: str):
    return re.sub(r"[^a-zA-Z0-9\-]", "", re.sub(r"[_\.\s\\/]", "-", "ltcards-" + string))

def field_injector(editor):
    # set notetype attribute for selective styles
    editor.web.eval("document.body.setAttribute('data-notetype', '{}')".format(editor.note.model()["name"]))

    inj_list = ["field_styles.css"]
    css_list = []
    js_list = []

    for inj_filename in inj_list:
        general_injector(inj_filename, css_list, js_list) # appends both versions from add-on own folder and from user_files directory

    field_selector = "div.editor-field .rich-text-editable"
    css_inject_template = """
        if (shadowRoot && !shadowRoot.getElementById("{css_id}")) {{
            const styleL = document.createElement("link");
            styleL.id = "{css_id}";
            styleL.rel = "stylesheet";
            styleL.href = "{css_filepath}";
            shadowRoot.appendChild(styleL);
        }}
    """
    js_inject_template = """
        if (shadowRoot && !shadowRoot.getElementById("{js_id}")) {{
            const scriptL = document.createElement("script");
            scriptL.id = "{js_id}";
            scriptL.type = "text/javascript";
            scriptL.src = "{js_filepath}";
            shadowRoot.appendChild(scriptL);
        }}
    """ # not recommended as the scripts are hoisted to the same level as editor_scripts

    injector_js = f"""
    function injector() {{
        fields = document.querySelectorAll("{field_selector}");
        fields.forEach(field => {{
            const shadowRoot = field.shadowRoot;
            {
                "\n".join(css_inject_template.format(
                    css_id=to_id(css_filepath), 
                    css_filepath=css_filepath
                ) for css_filepath in css_list)
                # + "\n".join(js_inject_template.format(
                #     js_id=to_id(js_filepath), 
                #     js_filepath=js_filepath
                # ) for js_filepath in js_list)
            }
        }});
        return(fields.length);
    }}
    if (injector() <= 0) {{
        new MutationObserver((mutation, observer) => {{
            if (document.querySelector("{field_selector}")) {{
                injector();
                observer.disconnect();
            }}
        }}).observe(document.body, {{ childList: true, subtree: true }});
    }}

    """

    editor.web.eval(injector_js)


gui_hooks.webview_will_set_content.append(window_injector)
# gui_hooks.editor_did_init.append(field_injector)
gui_hooks.editor_did_load_note.append(field_injector)
