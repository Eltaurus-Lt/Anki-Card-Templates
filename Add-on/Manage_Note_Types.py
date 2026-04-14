from anki import stdmodels
from anki.models import ModelManager
from aqt.utils import tr, getText
from . import Memrise_Cards

def basic_universal_model(col):

    noteTypeName, ok = getText(tr.actions_name(), default = "Basic (Lτ)")

    if not ok:
        return col.models.current() 

    mm = col.models
    noteType = mm.new(noteTypeName)

    # Fields
    mm.addField(noteType, mm.newField("Front"))
    mm.addField(noteType, mm.newField("Back"))
    mm.addField(noteType, mm.newField("Audio"))

    # Card Type
    cardType = mm.newTemplate("Card 1")
    cardType["qfmt"] = "<data>{{Back}}</data>{{Front}}"
    cardType["afmt"] = "{{FrontSide}}<hr id=answer>{{Back}}"
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