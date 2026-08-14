# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2024-2026 Eltaurus
# Contact: 
#     Email: Eltaurus@inbox.lt
#     GitHub: github.com/Eltaurus-Lt
#     Anki Forums: forums.ankiweb.net/u/Eltaurus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import re, textwrap

from aqt import mw
from anki.models import ModelManager
from aqt.utils import tooltip

from . import utils
from ...py.utils import files as file

from .Dialogs.Constructor import ConstructorDialog

mode_aliases = {
    "Typing": "typing",
    "Multiple-Choice": "mchoice",
    "Tapping": "tapping"
}

def insertAtAnchor(source_text, anchors, insert_text):

    lines = source_text.split("\n")

    for i, line in enumerate(lines):
        skip = False
        for anchor in anchors:
            if anchor not in line:
                skip = True
                continue
        if skip:
            continue

        insert_lines = insert_text.split("\n")
        base_indent = re.match(r"^[ \t]*", lines.pop(i)).group(0)
        insert_lines = [base_indent + insert_line for insert_line in insert_lines]

        lines.insert(i, "\n".join(insert_lines))
        break

    return "\n".join(lines)

def choicify(field_name):
    return "Choices " + field_name

def FrontHTML(cardType_data, fields_dict, theme = ""):
    def large_class(field_name):
        return " large" if fields_dict[field_name]["large"] else ""

    A = cardType_data["A"]
    Q = cardType_data["Q"]
    static_keys = fields_dict[A]["static"]
    random_keys = fields_dict[A]["random"]
    choices = choicify(A)
    prompt = cardType_data["prompt"]
    extra = cardType_data["Extra"]
    mode = mode_aliases[cardType_data["in"]]
    mch = mode == "mchoice"
    eq = fields_dict[A]["math"]

    if extra and extra != 'ー':
        extra_html = textwrap.dedent(f"""\
            {{{{#{extra}}}}}
                <div class="front-extra no-alts{large_class(extra)}">
                    <label>{extra}</label>
                    <span>{{{{{extra}}}}}</span>
                </div>
            {{{{/{extra}}}}}
        """).rstrip()
    else:
        extra_html = ""

    main_html = textwrap.dedent(f"""\
        {{{{#{Q}}}}}{{{{#{A}}}}}{ "{{#"+choices+"}}" if mch else "" }
        <setting id="static_keys">{static_keys}</setting>
        <setting id="random_keys">{random_keys}</setting>
        <data id="choices">{"{{"+choices+"}}" if mch else ""}</data>
        <data id="correctAnswer">{{{{{A}}}}}</data>

        <div class="card-content front{" nkeys" if mch else ""}{" eq" if eq else ""}" theme="{theme}" mode="{mode}">

            <div class="overhead">
                <div class="mem-instruction">
                    {prompt}
                </div>
                ⚓::Extra
            </div>

            <div class="mem-question no-alts memblob{large_class(Q)}">
                <div>{{{{{Q}}}}}</div>
            </div>

            <div class="mem-typing{large_class(A)}">
                <label>{A}</label>
                <input id="typeans" type="text" inputmode="text" autocorrect="off" autocomplete="off" autocapitalize="off" spellcheck="false">
            </div>

            <timer class="off"></timer>

            <div id="scr-keyboard" class="{large_class(A).strip()}">
                <div id="HintButton" class="membtn"><svg><path></path></svg>Hint</div>
            </div>

        </div>
        <a id="Lt" href="https://github.com/Eltaurus-Lt/Anki-Card-Templates" target="_blank"></a>
        { "{{/"+choices+"}}" if mch else "" }{{{{/{A}}}}}{{{{/{Q}}}}}
    """)

    return insertAtAnchor(main_html, ["⚓", "Extra"], extra_html)

def BackHTML(cardType_data, fields_data):

    A = cardType_data["A"]
    Q = cardType_data["Q"]

    large_dict = {}
    extra_html = ""
    for field in fields_data:
        name = field["Name"]
        if name not in large_dict:
            large_dict[name] = " large" if field["large"] else ""

        if name != A and name != Q and field["back"]:
            extra_html += textwrap.dedent(f"""
                {{{{#{name}}}}}
                    <div class="mem-field no-alts{large_dict[name]}">
                        <label>{name}</label>
                        <h4>{{{{{name}}}}}</h4>      
                    </div>
                {{{{/{name}}}}}
            """)

    main_html = textwrap.dedent(f"""\
        <hr id="answer" class="sys">
        <div id="backwrap" class="frontside">
            {{{{FrontSide}}}}
            <button id="mem-flip" class="sys">flip</button>
            <div class="card-content back">  

                <div class="mem-alert"></div>   

                <div class="mem-field{large_dict[A]}">
                    <label>{A}</label>
                    <h2>{{{{{A}}}}}</h2>
                    <span id="spelldiff" class="{large_dict[A].strip()}"></span>
                </div>

                <div class="mem-field no-alts{large_dict[Q]}">
                    <label>{Q}</label>
                    <h3>{{{{{Q}}}}}</h3>
                </div>

                <div class="sep"></div>
                ⚓::Extra
            </div>  
        </div>
    """)

    return insertAtAnchor(main_html, ["⚓", "Extra"], extra_html)

def FrontScript():
    return file.contents(f"Template/Front.js", __file__)

def BackScript():
    return file.contents(f"Template/Back.js", __file__)

def templateJoin(html, js):
    return html + textwrap.dedent("""



        <!-- -------------------⚙️ user prior scripts ⚙️------------------ -->
        <script>
          //place your scripts here


        </script>

        <!-- ---------------------  template scripts  --------------------- -->
    """) + js + textwrap.dedent("""

        <!-- -------------------⚙️ user posterior scripts ⚙️------------------ -->
        <script>
          //place your scripts here


        </script>
    """).rstrip()

def Styling():
    main_style = file.contents(f"Template/Styling.css", __file__)
    themes = "\n\n\n".join([utils.load_theme(theme) for theme in utils.list_themes(False)])

    return insertAtAnchor(main_style, ["⚓", "themes"], themes)



def Assemble(noteType_setup):
    mm = mw.col.models
    noteType = mm.new(f"Memrise (Lτ) v{utils.version()} | " + noteType_setup["Note Type"].strip())
    theme = noteType_setup["Theme"].replace("ー","")

    # Fields
    fields_dict = {}
    for field_data in noteType_setup["Fields"]:
        name = field_data["Name"]
        if name not in fields_dict:
            fields_dict[name] = field_data
            field = mm.new_field(name)
            mm.add_field(noteType, field)

    # Choice Fields
    mch_set = {cardType_data["A"] for cardType_data in noteType_setup["Card Types"] if mode_aliases[cardType_data["in"]] == "mchoice"}
    for field_data in noteType_setup["Fields"]:
        name = field_data["Name"]
        if name in mch_set:
            mch_set.remove(name)
            field = mm.new_field(choicify(name))
            field["collapsed"] = True
            field["excludeFromSearch"] = True
            mm.add_field(noteType, field)

    # Card Types
    pad_CTnames = len(noteType_setup["Card Types"]) != len({cardType_data["Name"] for cardType_data in noteType_setup["Card Types"]})
    for cardType_data in noteType_setup["Card Types"]:
        CTname = cardType_data["Name"]
        if pad_CTnames:
            CTname += " [" + cardType_data["in"] + "]" 
        cardType = mm.new_template(CTname)
        cardType["qfmt"] = templateJoin(FrontHTML(cardType_data, fields_dict, theme), FrontScript())
        cardType["afmt"] = templateJoin(BackHTML(cardType_data, noteType_setup["Fields"]), BackScript())
        mm.add_template(noteType, cardType)

    noteType["css"] = Styling()

    mm.add(noteType)
    mw.col.models.save(noteType)
    tooltip(f"Note Type \"{noteType_setup['Note Type']}\" successfully created")

    return noteType


def Setup(*args):
    dialog = ConstructorDialog()
    if dialog.exec():
        return Assemble(dialog.get_full_options())

    return mw.col.models.current()