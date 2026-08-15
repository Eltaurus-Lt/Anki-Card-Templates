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

from aqt import mw, gui_hooks
from aqt.webview import WebContent

from ..utils import inject


## Data

config = mw.addonManager.getConfig(__name__)


def inject_addon_config(web_content: WebContent, context: None):
    inject.json_content(config, web_content, tag_id="tau-config")


def inject_card_info(card):
    card_info = {
        "interval": card.ivl,
        "reviewCount": card.reps,
        "type": card.type # 0 = new, 1 = learning, 2 = review, 3 = relearning
    }
    # sm2
    if hasattr(card, "factor"):
        card_info["ease"] = card.factor
    # fsrs
    if hasattr(card, "memory_state"):
        if hasattr(card.memory_state, "difficulty"):
            card_info["difficulty"] = card.memory_state.difficulty
        if hasattr(card.memory_state, "stability"): # 90% interval
            card_info["stability"] = card.memory_state.stability

    inject.json(card_info, tag_id="card-info")


def inject_note_type(editor):
    inject.attr(
        "notetype",
        editor.note.model()["name"],
        editor.web
    )


gui_hooks.reviewer_did_show_question.append(inject_card_info)
gui_hooks.webview_will_set_content.append(inject_addon_config)
gui_hooks.editor_did_load_note.append(inject_note_type)



## Styles and Scripts

from aqt.deckbrowser import DeckBrowser
from aqt.overview import Overview
from aqt.editor import Editor
from aqt.reviewer import Reviewer
from aqt.browser.previewer import Previewer
from aqt.clayout import CardLayout


def window_injector(web_content: WebContent, context: None):
    inject.css_content("common_styles.css", web_content)
    inject.js_content("common_scripts.js", web_content)

    if isinstance(context, (DeckBrowser, Overview)):
        inject.css_content("deck_styles.css", web_content)
        inject.js_content("deck_scripts.js", web_content)

    if isinstance(context, DeckBrowser):
        inject.css_content("home_styles.css", web_content)
        inject.js_content("home_scripts.js", web_content)

    if isinstance(context, Overview):
        inject.css_content("overview_styles.css", web_content)
        inject.js_content("overview_scripts.js", web_content)

    if isinstance(context, Editor):
        inject.css_content("editor_styles.css", web_content)
        inject.js_content("editor_scripts.js", web_content)

    if isinstance(context, (Reviewer, Previewer, CardLayout)):
        inject.css_content("reviewer_styles.css", web_content)
        inject.js_content("reviewer_scripts.js", web_content)


def field_injector(editor):
    inject.shadowroot("div.editor-field .rich-text-editable", ["field_styles.css"], editor.web)


gui_hooks.webview_will_set_content.append(window_injector)
# gui_hooks.editor_did_init.append(field_injector)
gui_hooks.editor_did_load_note.append(field_injector)
