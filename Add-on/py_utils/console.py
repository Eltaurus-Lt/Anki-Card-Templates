from aqt.utils import tooltip

def log(msg, window = None):
    if window is None:
        tooltip('no web window')
        return

    window.web.eval(f'console.log(`{msg}`);')