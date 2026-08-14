def indexOf( array, el, default = 0 ):
        try:
            return array.index(el)
        except ValueError:
            return default