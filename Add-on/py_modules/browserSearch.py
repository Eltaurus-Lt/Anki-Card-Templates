from aqt import dialogs, gui_hooks, mw


def search_listener(handled, cmd, context):
    prefix = "Browser search::"
    if not cmd.startswith(prefix):
        return handled

    search_query = cmd[len(prefix):]
    browser = dialogs.open("Browser", mw)
    browser.form.searchEdit.lineEdit().setText(search_query)
    browser.onSearchActivated()
    return (True, None)


gui_hooks.webview_did_receive_js_message.append(search_listener)
