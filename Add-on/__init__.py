from . import MainUI, EditorUI
from .py import CardAPI, Backend

from aqt import mw
mw.addonManager.setWebExports(__name__, r"css/.*\.css|js/.*\.js|user_files/(.*\.(css|js))$")
