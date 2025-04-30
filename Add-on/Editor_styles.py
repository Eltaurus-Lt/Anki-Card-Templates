from aqt import gui_hooks, mw
from aqt.editor import Editor

addon_package = mw.addonManager.addonFromModule(__name__)
mw.addonManager.setWebExports(__name__, r"css/.*\.(css)$")
field_css = f"/_addons/{addon_package}/css/field_styles.css"

field_selector = "div.editor-field .rich-text-editable"

def inject_css_to_all_fields(editor):
    js_code = f"""
    function injectCSS() {{
        fields = document.querySelectorAll("{field_selector}");
        fields.forEach(field => {{
            const shadowRoot = field.shadowRoot;
            if (shadowRoot && !shadowRoot.getElementById("lt-field-style")) {{
                const styleLink = document.createElement("link");
                styleLink.id = "lt-field-style";
                styleLink.rel = "stylesheet";
                styleLink.href = "{field_css}";
                shadowRoot.appendChild(styleLink);
            }}
        }});
        return(fields.length);
    }}
    if (injectCSS() <= 0) {{
        new MutationObserver((mutation, observer) => {{
            if (document.querySelector("{field_selector}")) {{
                injectCSS();
                observer.disconnect();
            }}
        }}).observe(document.body, {{ childList: true, subtree: true }});
    }}

    """

    editor.web.eval(js_code)


# gui_hooks.editor_did_init.append(inject_css_to_all_fields)
gui_hooks.editor_did_load_note.append(inject_css_to_all_fields)
