import os
from aqt import gui_hooks
from aqt.editor import Editor

# Path to your CSS file
CSS_FILE_PATH = os.path.join(os.path.dirname(__file__), "custom_style.css")

def inject_css_to_all_fields(editor: Editor) -> None:
    """Inject the CSS file into the shadow DOM of all card fields in the editor."""
    js_code = f"""
    const fields = document.querySelectorAll("anki-editor-field");
    fields.forEach(field => {{
        const shadowRoot = field.shadowRoot;
        if (shadowRoot) {{
            const styleLink = document.createElement("link");
            styleLink.rel = "stylesheet";
            styleLink.href = "{CSS_FILE_PATH}";
            shadowRoot.appendChild(styleLink);
        }}
    }});
    """
    editor.web.eval(js_code)

# Hook into editor initialization to apply the changes
gui_hooks.editor_did_init.append(inject_css_to_all_fields)
