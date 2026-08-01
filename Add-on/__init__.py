from .py_modules import Clear_Shortcuts
from . import Editor_buttons
from .py_modules import Webview_injector
from . import Browser_Context_menu
from . import Top_Menu
from . import Manage_Note_Types
from .py_modules import Reviewer

from .py_modules import localStorage
from .py_modules import reviewerActions
from .py_modules import browserSearch

from aqt import mw
mw.addonManager.setWebExports(__name__, r"css/.*\.css|js/.*\.js|user_files/(.*\.(css|js))$")
