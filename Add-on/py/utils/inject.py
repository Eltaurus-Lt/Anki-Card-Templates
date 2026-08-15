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

import os, re, json as _json

from aqt import mw

from . import files


def _idify(name):
    return re.sub(r"[^a-zA-Z0-9\-]", "", re.sub(r"[_\.\s\\/]", "-", name))

def _texify(data):
    if isinstance(data, str):
        return data
    return _json.dumps(data)


## Appends to prepared web content

def css_content(css_file, web_content):
    if files.is_file(f"css/{css_file}"):
        web_content.css.append(files.url(f"css/{css_file}"))
    if files.is_file(f"user_files/{css_file}"):
        web_content.css.append(files.url(f"user_files/{css_file}"))


def js_content(js_file, web_content):
    if files.is_file(f"js/{js_file}"):
        web_content.js.append(files.url(f"js/{js_file}"))
    if files.is_file(f"user_files/{js_file}"):
        web_content.js.append(files.url(f"user_files/{js_file}"))


def json_content(data, web_content, tag_id = ""):
    id_attr = f" id='{_idify(tag_id)}'" if tag_id else ""
    web_content.head += f"<script type='application/json'{id_attr}>{_texify(data)}</script>"


## Injections to existing webview

def attr(key, value, webview):
    webview.eval(f"document.body.setAttribute('data-{key}', '{value}')")


def json(data, webview = None, tag_id = ""):
    if not tag_id:
        return
    tag_id = _idify(tag_id)

    if not webview:
        reviewer = mw.reviewer
        if not reviewer or not reviewer.web:
            return
        webview = reviewer.web

    webview.eval(f"""
        (()=>{{
            let scriptL = document.getElementById('{tag_id}');
            if (!scriptL) {{
                scriptL = document.createElement("script");
                scriptL.type = "application/json";
                scriptL.id = '{tag_id}';
                document.head.appendChild(scriptL);
            }}
            scriptL.textContent = '{_texify(data)}';
        }})();
    """)


def shadowroot(shadow_root_selector, css_list, webview):
    inject_template = """
        if (!shadowRoot.getElementById("{css_id}")) {{
            const styleL = document.createElement("link");
            styleL.id = "{css_id}";
            styleL.rel = "stylesheet";
            styleL.href = "{css_file}";
            shadowRoot.appendChild(styleL);
        }}
    """

    css_file_list = (
        [f"css/{css_file}" for css_file in css_list]
        + [f"user_files/{css_file}" for css_file in css_list]
    )

    webview.eval(f"""
        function field_css_injector() {{
            fields = document.querySelectorAll("{shadow_root_selector}");
            fields.forEach(field => {{
                const shadowRoot = field.shadowRoot;
                if (!shadowRoot) return;
                {
                    "\n".join(inject_template.format(
                        css_id=_idify(css_file), 
                        css_file=files.url(css_file)
                    ) for css_file in css_file_list if files.is_file(css_file))
                }
            }});
            return(fields.length);
        }}
        if (field_css_injector() <= 0) {{
            new MutationObserver((mutation, observer) => {{
                if (document.querySelector("{shadow_root_selector}")) {{
                    field_css_injector();
                    observer.disconnect();
                }}
            }}).observe(document.body, {{ childList: true, subtree: true }});
        }}

    """)