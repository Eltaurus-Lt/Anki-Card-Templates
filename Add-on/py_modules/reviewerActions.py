from aqt import gui_hooks, mw
from aqt.reviewer import Reviewer

def actions_listener(handled, cmd, context):
    if not isinstance(context, Reviewer):
        return handled

    # 1. Bury and Susupend
    if cmd == "action::bury_card":
        mw.reviewer.onBuryCard()
        return (True, None)
    if cmd == "action::bury_note":
        mw.reviewer.onBuryNote()
        return (True, None)
    if cmd == "action::suspend_card":
        mw.reviewer.onSuspendCard()
        return (True, None)
    if cmd == "action::suspend_note":
        mw.reviewer.onSuspend() # (sic!)
        return (True, None)

    # 2. Flag
    prefix = "action::flag::"
    if cmd.startswith(prefix):
        try:
            flag_i = int(cmd[len(prefix)])
            mw.reviewer.setFlag(flag_i)
        except ValueError:
            pass
        return (True, None)

    # 3. Undo
    if cmd == "action::undo":
        mw.onUndo()
        return (True, None)

    # 4. Voice actions
    if cmd == "action::voice_record":
        mw.reviewer.onRecordVoice()
        return (True, None)
    if cmd == "action::voice_replay":
        mw.reviewer.onReplayRecorded()
        return (True, None)
        
    return handled

gui_hooks.webview_did_receive_js_message.append(actions_listener)
