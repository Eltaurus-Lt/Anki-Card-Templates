from anki import stdmodels
from . import Basic, Memrise

# monkey-patch to anki note type manager
orig_get_stock_notetypes = stdmodels.get_stock_notetypes

def patched_get_stock_notetypes(*args, **kwargs):
    models = orig_get_stock_notetypes(*args, **kwargs)
    models.insert(4, ("Basic (Lτ)", Basic.Setup))
    models.insert(5, ("Memrise (Lτ)", Memrise.Setup))
    return models

stdmodels.get_stock_notetypes = patched_get_stock_notetypes