# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2024-2025 Eltaurus
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


import json, os
from aqt.qt import *
from PyQt6 import QtCore, QtWidgets
from aqt.utils import tooltip
from . import user_files
    
def create():
    dialog = NoteTypeCreator()
    if not dialog.exec():
        return
    noteType_data = dialog.get_full_options()

    tooltip(noteType_data)
    return



###  DIALOG

# refactor private/public variables


class NoScrollComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()

class NoteTypeCreator(QDialog):
    def getThemeList(self):
        themeList = user_files.list("Color Themes", ".css")
        themeList.insert(0, "ー")
        return themeList

    def updPresetList(self):
        self.presetList = user_files.list("Note Presets", ".json")
        if "default" in self.presetList:
            self.presetList.insert(0, self.presetList.pop(self.presetList.index("default")))

        self.preset.clear()
        self.preset.addItems(self.presetList)

    def presetNamechange(self):
        if self.preset.ignore_first:
            self.preset.ignore_first = False
            return
        if self.preset.currentText() in self.presetList:
            self.loadPreset()
            return

        # tooltip("preset renamed")
        self.markAsModified()

    def markAsModified(self):
        self.presave_button.setStyleSheet("""
            QPushButton { 
                border: 2px solid #FFA500;
            }
        """)
        return

    def markAsSaved(self):
        self.presave_button.setStyleSheet("""
            QPushButton { 
                border: 2px solid #0078D7;
            }
        """)
        return

    def modificationListener(self, table, row):
        for col in range(table.columnCount()):
            widget = table.cellWidget(row, col)
            if isinstance(widget, QWidget) and widget.layout():
                item = widget.layout().itemAt(0)
                if item is not None:
                    widget = item.widget()
            if isinstance(widget, QLineEdit):
                widget.textChanged.connect(self.markAsModified)
            elif isinstance(widget, QCheckBox):
                widget.stateChanged.connect(self.markAsModified)
            elif isinstance(widget, NoScrollComboBox):
                widget.currentIndexChanged.connect(self.markAsModified)

    def savePreset(self):
        preset_json = json.dumps(self.get_preset_options(), indent=4)
        user_files.save(f"Note Presets/{self.preset.currentText()}.json", preset_json)

        currentPreset = self.preset.currentText() 
        if currentPreset not in self.presetList:
            self.updPresetList()
            ind = self.indexOf(self.presetList, currentPreset)
            if ind == 0:
                tooltip('error saving the preset')
            else:
                tooltip('New preset saved')
            self.preset.setCurrentIndex(ind)
        else:
            tooltip('Preset saved')

        self.markAsSaved()

    def deletePreset(self):
        return

    def loadPreset(self):
        # if modified: warning...
        preset_json = user_files.load(f"Note Presets/{self.preset.currentText()}.json")
        if preset_json is None:
            tooltip(f"error loading {preset} file")
            return

        preset = json.loads(preset_json)

        for r in range(self.fieldsTable.rowCount()):
            self.fieldsTable.removeRow(0)
        for r in range(self.cardTypes.rowCount()):
            self.cardTypes.removeRow(0)

        for field in preset["Fields"]:
            self.add_field(field)
        for cardType in preset["Card Types"]:
            self.add_cardType(cardType)

        self.markAsSaved()
        

    def indexOf(self, array, el, default = 0):
        try:
            return array.index(el)
        except ValueError:
            return default

    def toggleCellCheckbox(self, cellWidget):
        if cellWidget:
            checkbox = cellWidget.findChild(QCheckBox)
            if checkbox:
                checkbox.setChecked(not checkbox.isChecked())

    def setHeadersWithTooltips(self, table, headersWithTooltips):
        for i, (header, tooltip) in enumerate(headersWithTooltips):
            header_widget = QTableWidgetItem(header)
            if tooltip is not None:
                header_widget.setToolTip(tooltip)
            table.setHorizontalHeaderItem(i, header_widget)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (16777220, 16777221): # 'Enter' codes
            event.ignore()
        else:
            super().keyPressEvent(event)


    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QHeaderView::section:horizontal { padding: 0; }
            QHeaderView::section:vertical { padding: 7px; }
            QTableCornerButton::section { background: #73c7f4; }
            QTableWidget::item {  }
            QCheckBox { padding-left: 7px; }
            QToolTip {  }
            QHeaderView::section { 
                color: white; 
                background: #73c7f4; 
                font-weight: bold; 
                font-size: 15px; 
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Note Type Creator")

        self.noteType = QLineEdit("New Note Type") #Memrise (Lτ) 
        self.noteType.setToolTip("<nobr>Name for the created Note Type</nobr><br><i>e.g.</i> \"Greek\", \"History\", <nobr>\"Spanish (no audio)\", or</nobr><br>\"Geography (multiple-choice)\"")
        self.noteType.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.noteType)

        font_metrics = QFontMetrics(self.noteType.font())
        lh = font_metrics.lineSpacing()

        self.resize(50 * lh, 35 * lh)
        self.setMinimumWidth(35 * lh)

        # Presets
        preset_layout = QHBoxLayout()

        preset_layout.addWidget(QLabel("Color Theme:"))
        self.theme = QComboBox()
        self.theme.setToolTip("Color theme for all Card Types")
        themeList = self.getThemeList()
        self.theme.addItems(themeList)
        theme_index = self.indexOf(themeList, "Memrise", self.indexOf(themeList, "Anki", 1))
        self.theme.setCurrentIndex(theme_index)
        self.theme.setFixedWidth(7 * lh)
        preset_layout.addWidget(self.theme)

        preset_layout.addStretch()

        preset_layout.addWidget(QLabel("Preset:"))
        self.preset = NoScrollComboBox()
        self.preset.setToolTip("Note Type preset<hr><nobr>Select from the dropdown menu to load</nobr><br><i>or</i><br>Type in a new name and click 'Save' to create a new one")
        self.updPresetList()
        self.preset.setFixedWidth(10 * lh)
        self.preset.setEditable(True)
        # self.preset.setCurrentIndex(0)
        # self.preset.lineEdit().setText(self.preset.currentText())
        # self.preset.clearFocus()
        # self.preset.lineEdit().clearFocus()
        self.preset.ignore_first = True
        self.preset.lineEdit().editingFinished.connect(self.presetNamechange)
        self.preset.currentIndexChanged.connect(lambda: self.preset.clearFocus())
        # self.preset.editTextChanged.connect(self.renamePreset)
        preset_layout.addWidget(self.preset)

        self.presave_button = QPushButton("Save")
        self.presave_button.setToolTip("Save current profile under the currently selected preset name<hr>⚠️ overwrites profile with the same name if it already exist")
        # self.presave_button.setAutoDefault(False)
        self.presave_button.clicked.connect(self.savePreset)
        preset_layout.addWidget(self.presave_button)

        layout.addLayout(preset_layout)


        # Fields setup
        fields_group = QGroupBox("Fields")
        fields_layout = QVBoxLayout()
        fields_group.setLayout(fields_layout)        
        self.fieldsTable = QTableWidget(0, 7)
        self.setHeadersWithTooltips(self.fieldsTable, [
            ("Field Label",'<nobr>Memrise\'s "(Column) <b>Name</b>" and "(Column) <b>Label</b>"</nobr><hr>An informative, short name for the Field to be labeled as in the Anki Editor and on the Cards'),
            ("Big",'<nobr>Memrise\'s "<b>Show Bigger</b>"</nobr><hr>This will make the text a bit bigger in the learning experience. Useful for <i>e.g.</i> Chinese. For Audio this will increase the size of the button when used as Question.'),
            ("Back",'<nobr>Memrise\'s "<b>Always Show</b>"</nobr><hr>This Field will always be displayed on the back, even when not being set as Question, Answer, or Front Extra, without the learner needing to click \'Browse\'.'),
            ("Math",'<nobr>non-Memrise setting</nobr><hr>Enable for Fields intended to contain LaTeX (MathJax) equations so that they can be properly autorated when used as Answers'),
            ("Static Keys",'<nobr>Memrise\'s "<b>Keyboard Characters</b>"</nobr><hr>If this contains characters, they will form the <nobr>on-screen</nobr> keyboard used in the learning experience.'),
            ("Random Keys",'<nobr>Memrise\'s "<b>predefined keyboard</b>"</nobr><hr>An alphabet or similar list of most-used characters to randomize the <nobr>on-screen</nobr> keyboard\'s set of keys'),
            ("", None)])
        self.fieldsTable.horizontalHeader().setMinimumSectionSize(2 * lh)
        self.fieldsTable.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.NoSelection)
        self.fieldsTable.cellClicked.connect(lambda r, c: self.toggleCellCheckbox(self.fieldsTable.cellWidget(r, c)))
        self.fieldsTable.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.fieldsTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.fieldsTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        fields_layout.addWidget(self.fieldsTable)
        underfields_layout = QHBoxLayout()
        underfields_layout.addStretch()
        self.addField_button = QPushButton("+")
        self.addField_button.setFixedWidth(3 * lh)
        self.addField_button.clicked.connect(lambda: self.add_field({}))
        underfields_layout.addWidget(self.addField_button)
        fields_layout.addLayout(underfields_layout)
        self.addField_button.setToolTip("Add new Field")

        layout.addWidget(fields_group)

        # Card Types setup
        cardTypes_group = QGroupBox("Card Types")
        cardTypes_layout = QVBoxLayout()
        cardTypes_group.setLayout(cardTypes_layout)
        self.cardTypes = QTableWidget(0, 8)
        self.setHeadersWithTooltips(self.cardTypes, [
            ("Card Type","An informative, short name<br> for identifying the Card Type in Anki Browser and Card Template Editor"),
            ("Question",'<nobr>Memrise\'s "<b>Prompt With</b>"</nobr><hr>This is the Field that will be presented as the Card\'s question. Using a Field containing audio as the Question will turn the Card into a Listening Card'),
            ("Answer",'<nobr>Memrise\'s "<b>Test On</b>"</nobr><hr>This is the Field that learners will have to answer with on tests'),
            ("Input","<nobr>The method for the Answer to be input with</nobr><hr>Memrise's <b>enabling Typing and Tapping Tests</b> is equivalent to cloning a Card Type and changing its Input method<br><b>Disabling</b> either of the Tests is equivalent to deleting the respective Card Type"),
            ("Prompt","A short text instruction that will<br> be shown above the Question<br>(not customizable on Memrise)"),
            ("Front Extra",'<nobr>Memrise\'s "<b>first always&#8209;show text column</b>"</nobr><hr>This is a Field that will appear as extra information after a test, replacing the Prompt when answer is submitted'),
            ("", None), ("", None)])
        self.cardTypes.horizontalHeader().setMinimumSectionSize(2 * lh)
        self.cardTypes.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cardTypes.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.cardTypes.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        cardTypes_layout.addWidget(self.cardTypes)

        layout.addWidget(cardTypes_group)

        self.loadPreset()


        # set table columns
        self.fieldsTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.fieldsTable.setColumnWidth(0, 10 * lh)
        self.fieldsTable.setColumnWidth(1, 2.5 * lh)
        self.fieldsTable.setColumnWidth(2, 2.5 * lh)
        self.fieldsTable.setColumnWidth(3, 2.5 * lh)
        self.fieldsTable.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.fieldsTable.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.fieldsTable.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.fieldsTable.setColumnWidth(6, 2 * lh)

        self.cardTypes.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.cardTypes.setColumnWidth(0, 8 * lh)
        self.cardTypes.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.cardTypes.setColumnWidth(1, 6 * lh)
        self.cardTypes.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.cardTypes.setColumnWidth(2, 6 * lh)
        self.cardTypes.setColumnWidth(3, 6 * lh)
        self.cardTypes.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.cardTypes.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.cardTypes.setColumnWidth(5, 6 * lh)        
        self.cardTypes.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.cardTypes.setColumnWidth(6, 2 * lh)
        self.cardTypes.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.cardTypes.setColumnWidth(7, 2 * lh)


        # Ok/Cancel
        button_ok = QPushButton("Create")
        button_ok.clicked.connect(self.accept)
        button_cancel = QPushButton("Cancel")
        button_cancel.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(button_ok)
        button_layout.addWidget(button_cancel)

        layout.addLayout(button_layout)

        # Styling
        #self.fieldsTable.setShowGrid(False)
        self.cardTypes.setShowGrid(False)
        #self.cardTypes.setStyleSheet("QTableWidget { background-color: transparent; }")
        # self.cardTypes.resizeColumnsToContents()
        

    def field_row2dic(self, row):

        return {
            "Name": self.fieldsTable.cellWidget(row, 0).text(),
            "large": self.fieldsTable.cellWidget(row, 1).layout().itemAt(0).widget().isChecked(),
            "back": self.fieldsTable.cellWidget(row, 2).layout().itemAt(0).widget().isChecked(),
            "math": self.fieldsTable.cellWidget(row, 3).layout().itemAt(0).widget().isChecked(),
            "static": self.fieldsTable.cellWidget(row, 4).text(),
            "random": self.fieldsTable.cellWidget(row, 5).text(),
        }

    def add_field(self, params):
        row = self.fieldsTable.rowCount()
        self.fieldsTable.setRowCount(row + 1)

        field_name = params.get("Name", f"Field {row+1}")
        name = QLineEdit(field_name)
        name.setCursorPosition(0)
        self.fieldsTable.setCellWidget(row, 0, name)
        name.textChanged.connect(self.rename_field)

        large = QCheckBox()
        large.setChecked(params.get("large", False))
        checkbox_cell = QWidget()
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_cell.setLayout(checkbox_layout)
        checkbox_layout.addWidget(large)
        self.fieldsTable.setCellWidget(row, 1, checkbox_cell)

        back = QCheckBox()
        back.setChecked(params.get("back", True))
        checkbox_cell = QWidget()
        checkbox_layout = QHBoxLayout()
        # back.setStyleSheet("QCheckBox { margin-left: 10px; }")
        checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        # checkbox_cell.setStyleSheet("margin-left: 10px")
        # checkbox_layout.setSpacing(0)
        checkbox_cell.setLayout(checkbox_layout)
        checkbox_layout.addWidget(back)
        self.fieldsTable.setCellWidget(row, 2, checkbox_cell)

        math = QCheckBox()
        math.setChecked(params.get("math", False))
        checkbox_cell = QWidget()
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_cell.setLayout(checkbox_layout)
        checkbox_layout.addWidget(math)
        self.fieldsTable.setCellWidget(row, 3, checkbox_cell)

        static = QLineEdit(params.get("static", ""))
        static.setCursorPosition(0)
        self.fieldsTable.setCellWidget(row, 4, static)

        random = QLineEdit(params.get("random", ""))
        random.setCursorPosition(0)
        self.fieldsTable.setCellWidget(row, 5, random)

        # Add remove button
        remove_button = QPushButton("-")
        remove_button.setToolTip("Delete the Field")
        remove_button.clicked.connect(self.remove_field)
        self.fieldsTable.setCellWidget(row, self.fieldsTable.columnCount()-1, remove_button)

        # Add the respective item to qboxes for each card type
        for r in range(self.cardTypes.rowCount()):
            self.cardTypes.cellWidget(r, 1).addItem(field_name) #question
            self.cardTypes.cellWidget(r, 2).addItem(field_name) #answer
            self.cardTypes.cellWidget(r, 5).addItem(field_name) #extra

        self.modificationListener(self.fieldsTable, row)
        self.markAsModified()

    def rename_field(self):
        sender_field = self.sender()

        for r in range(self.fieldsTable.rowCount()):
            if self.fieldsTable.cellWidget(r, 0) == sender_field:
                break
        new_name = self.fieldsTable.cellWidget(r, 0).text()

        # Rename the respective item in qboxes for each card type
        for rC in range(self.cardTypes.rowCount()):
            self.cardTypes.cellWidget(rC, 1).setItemText(r, new_name) #question
            self.cardTypes.cellWidget(rC, 2).setItemText(r, new_name) #question
            self.cardTypes.cellWidget(rC, 5).setItemText(r+1, new_name) #question

    def remove_field(self):
        sender_button = self.sender()

        if self.fieldsTable.rowCount() <= 2:
            return

        for r in range(self.fieldsTable.rowCount()):
            if self.fieldsTable.cellWidget(r, self.fieldsTable.columnCount()-1) == sender_button:
                break

        # tooltip(f'removed row {r}')                
        self.fieldsTable.removeRow(r)

        # Remove the respective item from qboxes for each card type
        for rC in range(self.cardTypes.rowCount()):
            self.cardTypes.cellWidget(rC, 1).removeItem(r) #question
            self.cardTypes.cellWidget(rC, 2).removeItem(r) #answer
            self.cardTypes.cellWidget(rC, 5).removeItem(r+1) #extra

        self.markAsModified()


    def add_cardType(self, params):
        row = self.cardTypes.rowCount()
        self.cardTypes.setRowCount(row + 1)

        name = QLineEdit(params.get("Name", f"Card {row+1}"))
        name.setCursorPosition(0)
        self.cardTypes.setCellWidget(row, 0, name)

        current_fields = [self.fieldsTable.cellWidget(r, 0).text() for r in range(self.fieldsTable.rowCount())]

        question = NoScrollComboBox()
        question.addItems(current_fields)
        question_index = self.indexOf(current_fields, params.get("Q"), 1)
        question.setCurrentIndex(question_index)        
        self.cardTypes.setCellWidget(row, 1, question)

        answer = NoScrollComboBox()
        answer.addItems(current_fields)
        answer_index = self.indexOf(current_fields, params.get("A"), 0)
        answer.setCurrentIndex(answer_index)      
        self.cardTypes.setCellWidget(row, 2, answer)


        input_methods = ["Typing", "Multiple-Choice", "Tapping"]
        input_tooltips = [
            "Type the answer using physical, mobile or the template's on-screen keyboard<hr>The most rigorous form of testing, effective for building strong memory", 
            "Select the correct answer out of several suggested options<hr>Good for introductory testing, tests with image answers, or for disambiguating between commonly confused words (if Choices are added manually)", 
            "Arrange words in the correct order by tapping them<hr><nobr>Good for getting used to Language</nobr> grammar with sentence Cards"
            ]
        inputMethod = NoScrollComboBox()
        # inputMethod.addItems(input_methods)
        for i, input_method in enumerate(input_methods):
            inputMethod.addItem(input_method)
            inputMethod.setItemData(i, input_tooltips[i], QtCore.Qt.ItemDataRole.ToolTipRole)
        current_method = self.indexOf(input_methods, params.get("in"))
        inputMethod.setCurrentIndex(current_method)
        self.cardTypes.setCellWidget(row, 3, inputMethod)

        prompt = QLineEdit(params.get("prompt", ""))
        prompt.setCursorPosition(0)
        prompt_opacity = QGraphicsOpacityEffect()
        prompt_opacity.setOpacity(0.5)
        prompt.setGraphicsEffect(prompt_opacity)
        self.cardTypes.setCellWidget(row, 4, prompt)

        extra_options = ["ー"] + current_fields
        front_extra = NoScrollComboBox()
        front_extra.addItems(extra_options)
        extra_index = self.indexOf(extra_options, params.get("Extra"))
        front_extra.setCurrentIndex(extra_index)
        self.cardTypes.setCellWidget(row, 5, front_extra)        

        # Add remove button
        remove_button = QPushButton("-")
        remove_button.setToolTip("Delete the Card Type")
        remove_button.clicked.connect(self.remove_cardType)
        self.cardTypes.setCellWidget(row, self.cardTypes.columnCount()-2, remove_button)

        # Add clone button
        clone_button = QPushButton("↓+")
        clone_button.setToolTip("Clone the Card Type")
        clone_button.clicked.connect(self.clone_cardType)
        self.cardTypes.setCellWidget(row, self.cardTypes.columnCount()-1, clone_button)

        self.modificationListener(self.cardTypes, row)

    def card_row2dic(self, row):

        return {
            "Name": self.cardTypes.cellWidget(row, 0).text(),
            "Q": self.cardTypes.cellWidget(row, 1).currentText(),
            "A": self.cardTypes.cellWidget(row, 2).currentText(),
            "in": self.cardTypes.cellWidget(row, 3).currentText(),
            "prompt": self.cardTypes.cellWidget(row, 4).text(),
            "Extra": self.cardTypes.cellWidget(row, 5).currentText()
        }

    def clone_cardType(self):
        sender_button = self.sender()

        for r in range(self.cardTypes.rowCount()):
            if self.cardTypes.cellWidget(r, self.cardTypes.columnCount()-1) == sender_button:
                # tooltip(f'cloned row {r}')

                params = self.card_row2dic(r)
                # params.pop("Name", None)
                # params.pop("prompt", None)

                self.add_cardType(params)
                break

        self.markAsModified()

    def remove_cardType(self):
        sender_button = self.sender()

        if self.cardTypes.rowCount() <= 1:
            return

        for r in range(self.cardTypes.rowCount()):
            if self.cardTypes.cellWidget(r, self.cardTypes.columnCount()-2) == sender_button:
                # tooltip(f'removed row {r}')
                self.cardTypes.removeRow(r)
                break

        self.markAsModified()

    def get_preset_options(self):
        fields = [self.field_row2dic(r) for r in range(self.fieldsTable.rowCount())]
        card_types = [self.card_row2dic(r) for r in range(self.cardTypes.rowCount())]

        return {"Fields": fields, "Card Types": card_types}

    def get_full_options(self):
        options = self.get_preset_options()
        options["Note Type"] = self.noteType.text()
        options["Theme"] = self.theme.currentText()

        return options