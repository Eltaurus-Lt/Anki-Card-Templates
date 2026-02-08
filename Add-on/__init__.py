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

def contextual_injector(web_content: WebContent, context: None):
    def inject(inj_filename):
        inj_type = os.path.splitext(inj_filename)[1].lstrip(".").lower()

        if inj_type == "css":
            target = web_content.css
        elif inj_type == "js":
            target = web_content.js
        else:
            return

        if os.path.exists(os.path.join(addons_folder, addon_name, inj_type, inj_filename)):
            target.append(f"/_addons/{addon_name}/{inj_type}/{inj_filename}")
        if os.path.exists(os.path.join(addons_folder, addon_name, "user_files", inj_filename)):
            target.append(f"/_addons/{addon_name}/user_files/{inj_filename}")

    if isinstance(context, (DeckBrowser, Overview)):
        inject("deck_styles.css")


gui_hooks.webview_will_set_content.append(contextual_injector)
