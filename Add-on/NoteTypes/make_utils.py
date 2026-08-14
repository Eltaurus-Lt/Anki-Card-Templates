def wrapScript(js_contents):
    return (
            '\n'
            '\n'
            '<script>\n'
            f'{js_contents}\n'
            '</script>\n'
           )