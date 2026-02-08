from . import Clear_Shortcuts
from . import Editor_buttons
from . import Editor_styles
from . import Browser_Context_menu
from . import Tools_Menu


from aqt import gui_hooks, mw
from aqt.deckbrowser import DeckBrowser
from aqt.overview import Overview
from aqt.webview import WebContent
import os

mw.addonManager.setWebExports(__name__, r"css/.*\.css|js/.*\.js|user_files/(.*\.(css|js))$")
addons_folder = mw.addonManager.addonsFolder()
addon_name = mw.addonManager.addonFromModule(__name__)


def inject_to_deck_browser(web_content: WebContent, context: None):
    if isinstance(context, (DeckBrowser, Overview)):
        web_content.css.append(f"/_addons/{addon_name}/css/deck_styles.css")
        if os.path.exists(os.path.join(addons_folder, addon_name, "user_files", "deck_styles.css")):
            web_content.css.append(f"/_addons/{addon_name}/user_files/deck_styles.css")


gui_hooks.webview_will_set_content.append(inject_to_deck_browser)
