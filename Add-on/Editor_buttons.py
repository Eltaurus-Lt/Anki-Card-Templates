import os, json
from anki.hooks import addHook
from aqt.utils import tooltip
from . import console

addon_path = os.path.dirname(__file__)

def alts_format_old(editor):
    selection = editor.web.selectedText()
    if selection:
        alt_section = '<span part="alt">' + selection + '</span>'
        editor.web.eval(f"document.execCommand('insertHTML', false, {repr(alt_section)});")


def alts_format(editor):
    current_field = editor.currentField
    if current_field is None:
        tooltip('No field selected')
        return

    js_code = """
        (function() {
            try {    
                const activeElement = document.activeElement;
                const shadowRoot = activeElement.shadowRoot;
                const field = shadowRoot.querySelector('[contenteditable="true"]');
                const fieldContent0 = field.innerHTML;

                const selection = shadowRoot.getSelection();
                console.log(selection);
                if (selection.rangeCount > 0) {
                    const range = selection.getRangeAt(0);
                    const altDiv = document.createElement('div');
                    altDiv.setAttribute("part", "alt");
                    altDiv.appendChild(range.extractContents());
                    range.insertNode(altDiv);
                }

                const fieldContent = field.innerHTML;

                return JSON.stringify({
                    fieldContent: fieldContent
                });
            } catch (error) {
                return JSON.stringify({ error: error.message });
            }
        })();
    """

    def callback(js_result):
        try:
            result = json.loads(js_result)
            if result.get("error"):
                console.log(result["error"], editor)
                if result["error"] == "Cannot read properties of null (reading 'querySelector')":
                    tooltip("formatted field content should be selected instead of html code")
                return

            # # clean editor's stray <br>
            # fieldContent = result["fieldContent"][:-4] if result["fieldContent"].endswith("<br>") else result["fieldContent"]

            # cf = ( fieldContent == editor.note.fields[current_field])
            # if not cf:
            #     console.log(editor.note.fields[current_field], editor)
            #     console.log(fieldContent, editor)
            #     tooltip("error comparing field content with editor's webview")
                

        except json.JSONDecodeError:
            editor.web.eval("alert('An error occurred while processing the selection!')")

    editor.web.evalWithCallback(js_code, callback)

def setupEditorButtonsFilter(buttons, editor):
    buttons.insert(0,
        editor.addButton(
            os.path.join(addon_path, "icons", "alts.svg"),
            'alts',
            alts_format,
            tip = "Format as an alternative"
        )
    )

    return buttons

addHook("setupEditorButtons", setupEditorButtonsFilter)