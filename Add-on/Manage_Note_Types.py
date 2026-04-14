from anki import stdmodels
from anki.models import ModelManager
from aqt.utils import tr, getText
from . import Memrise_Cards
from .py_utils import user_files

def insertJS(script_name):
    return (
            '\n'
            '\n'
            '<script>\n'
            f'{user_files.load("Source code/"+script_name+".js")}\n'
            '</script>\n'
           )

def basic_universal_model(col):

    noteTypeName, ok = getText(tr.actions_name(), default = "Basic (Lτ)")

    if not ok:
        return col.models.current() 

    mm = col.models
    noteType = mm.new(noteTypeName)

    # Fields
    mm.addField(noteType, mm.newField("Front"))
    mm.addField(noteType, mm.newField("Back"))

    # Card Type
    cardType = mm.newTemplate("Card 1")
    cardType["qfmt"] = (
                        '<data id="expans">{{Back}}</data>\n'
                        '\n'
                        '{{Front}}\n'
                        '\n'
                        '<input id="typeans" type="text" inputmode="text" autocorrect="off" autocomplete="off" autocapitalize="off" spellcheck="false">\n'
                        f"{insertJS('Cross-platform Typing (front)')}"
                        f"{insertJS('AnkiWeb audio')}"
                       )
    cardType["afmt"] = (
                        '{{Front}}\n'
                        '\n'
                        '<hr id=answer>\n'
                        '\n'
                        '<input id="typeans">\n'
                        f"{insertJS('Cross-platform Typing (back)')}"
                        f"{insertJS('AnkiWeb audio')}"
                       )
    noteType["css"] = (
                        f'{user_files.load("Source code/common.css")}\n'
                        '\n'
                        f'{user_files.load("Source code/style resets.css")}\n'
                        '\n'
                        '\n'
                        '\n'
                        '/* card styling */\n' 
                        '\n'
                        '.card {\n'
                        '    font-family: arial;\n'
                        '    font-size: 20px;\n'
                        '    line-height: 1.5;\n'
                        '    text-align: center;\n'
                        '    color: black;\n'
                        '}'
                       )
    mm.addTemplate(noteType, cardType)

    # Add to the collection
    mm.add(noteType)
    mm.save(noteType)

    return noteType


# monkey-patch to the note manager
orig_get_stock_notetypes = stdmodels.get_stock_notetypes

def patched_get_stock_notetypes(*args, **kwargs):
    models = orig_get_stock_notetypes(*args, **kwargs)
    models.insert(4, ("Basic (Lτ)", basic_universal_model))
    models.insert(5, ("Memrise (Lτ)", Memrise_Cards.create))
    return models

stdmodels.get_stock_notetypes = patched_get_stock_notetypes