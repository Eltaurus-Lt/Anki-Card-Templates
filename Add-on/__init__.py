from . import Clear_Shortcuts
from . import Fill_Choices_menu
from . import Editor_buttons

from aqt import gui_hooks, mw
from aqt.editor import Editor
from aqt.webview import AnkiWebView, WebContent


mw.addonManager.setWebExports(__name__, r"css/.*\.(css)$")
addon_package = mw.addonManager.addonFromModule(__name__)

def inject_editor_styles(web_content: WebContent, context: None):
    if isinstance(context, Editor):
        web_content.css.append(f"/_addons/{addon_package}/css/editor_styles.css")


gui_hooks.webview_will_set_content.append(inject_editor_styles)