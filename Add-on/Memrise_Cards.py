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

# preset renaming and saving
# TeX checkbox + preset

# refactor private/public variables
# onhover tooltips (+column headers)

class NoteTypeCreator(QDialog):
    def getThemeList(self):
        theme_list = user_files.list("Color Themes", ".css")
        theme_list.insert(0, "ー")
        return theme_list

    def getPresetList(self):
        preset_list = user_files.list("Note Presets", ".json")
        if "default" in preset_list:
            preset_list.insert(0, preset_list.pop(preset_list.index("default")))
        return preset_list

    def renamePreset(self):
        tooltip("preset renamed")

    def setAsModified(self):
        return

    def setAsSaved(self):
        return

    def savePreset(self):
        preset_json = json.dumps(self.get_preset_options(), indent=4)
        user_files.save(f"Note Presets/{self.preset.currentText()}.json", preset_json)

    def loadPreset(self):
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

    def __init__(self):
        super().__init__()

        tableStyle = """
            QHeaderView::section:horizontal { padding: 0; }
            QHeaderView::section:vertical { padding: 7px; }
            QHeaderView::section { color: white; background: #73c7f4; font-weight: bold; font-size: 15px; }
            QTableCornerButton::section { background: #73c7f4; }
            QTableWidget::item {  }
            QCheckBox { padding-left: 7px; }
        """

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Note Type Creator")

        self.noteType = QLineEdit("New Note Type") #Memrise (Lτ) 
        self.noteType.setToolTip("Name of the created Note Type<br><i>e.g.</i> \"Chinese (typing only)\", or \"Geography\"")
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
        theme_list = self.getThemeList()
        self.theme.addItems(theme_list)
        theme_index = self.indexOf(theme_list, "Memrise", self.indexOf(theme_list, "Anki", 1))
        self.theme.setCurrentIndex(theme_index)
        self.theme.setFixedWidth(7 * lh)
        preset_layout.addWidget(self.theme)

        preset_layout.addStretch()

        preset_layout.addWidget(QLabel("Preset:"))
        self.preset = QComboBox()
        self.preset.addItems(self.getPresetList())
        self.preset.setFixedWidth(10 * lh)
        self.preset.setEditable(True)
        # self.preset.lineEdit().editingFinished.connect(self.renamePreset)
        self.preset.currentIndexChanged.connect(self.loadPreset)
        self.preset.editTextChanged.connect(self.renamePreset)
        preset_layout.addWidget(self.preset)

        button_presave = QPushButton("Save")
        button_presave.clicked.connect(self.savePreset)
        preset_layout.addWidget(button_presave)

        layout.addLayout(preset_layout)


        # Fields setup
        fields_group = QGroupBox("Fields")
        fields_layout = QVBoxLayout()
        fields_group.setLayout(fields_layout)        
        self.fieldsTable = QTableWidget(0, 6)
        self.fieldsTable.setHorizontalHeaderLabels(["Field Label", "Big", "Back", "Static Keys", "Random Keys", ""])
        self.fieldsTable.horizontalHeader().setMinimumSectionSize(2 * lh)
        self.fieldsTable.setStyleSheet(tableStyle)
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
        self.cardTypes.setHorizontalHeaderLabels(["Card Type", "Question", "Answer", "Input", "Prompt", "Front Extra", "", ""])
        self.cardTypes.horizontalHeader().setMinimumSectionSize(2 * lh)
        self.cardTypes.setStyleSheet(tableStyle)
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
        self.fieldsTable.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.fieldsTable.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.fieldsTable.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.fieldsTable.setColumnWidth(5, 2 * lh)

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
            "static": self.fieldsTable.cellWidget(row, 3).text(),
            "random": self.fieldsTable.cellWidget(row, 4).text(),
        }

    def add_field(self, params):
        row = self.fieldsTable.rowCount()
        self.fieldsTable.setRowCount(row + 1)

        field_name = params.get("Name", f"Field {row+1}")
        name = QLineEdit(field_name)
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

        static = QLineEdit(params.get("static", ""))
        self.fieldsTable.setCellWidget(row, 3, static)

        random = QLineEdit(params.get("random", ""))
        self.fieldsTable.setCellWidget(row, 4, random)

        # Add remove button
        remove_button = QPushButton("-")
        remove_button.clicked.connect(self.remove_field)
        self.fieldsTable.setCellWidget(row, self.fieldsTable.columnCount()-1, remove_button)

        # Add the respective item to qboxes for each card type
        for r in range(self.cardTypes.rowCount()):
            self.cardTypes.cellWidget(r, 1).addItem(field_name) #question
            self.cardTypes.cellWidget(r, 2).addItem(field_name) #answer
            self.cardTypes.cellWidget(r, 5).addItem(field_name) #extra

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

        tooltip(f'removed row {r}')                
        self.fieldsTable.removeRow(r)

        # Remove the respective item from qboxes for each card type
        for rC in range(self.cardTypes.rowCount()):
            self.cardTypes.cellWidget(rC, 1).removeItem(r) #question
            self.cardTypes.cellWidget(rC, 2).removeItem(r) #answer
            self.cardTypes.cellWidget(rC, 5).removeItem(r+1) #extra


    def add_cardType(self, params):
        row = self.cardTypes.rowCount()
        self.cardTypes.setRowCount(row + 1)

        name = QLineEdit(params.get("Name", f"Card {row+1}"))
        self.cardTypes.setCellWidget(row, 0, name)

        current_fields = [self.fieldsTable.cellWidget(r, 0).text() for r in range(self.fieldsTable.rowCount())]

        question = QComboBox()
        question.addItems(current_fields)
        question_index = self.indexOf(current_fields, params.get("Q"), 1)
        question.setCurrentIndex(question_index)        
        self.cardTypes.setCellWidget(row, 1, question)

        answer = QComboBox()
        answer.addItems(current_fields)
        answer_index = self.indexOf(current_fields, params.get("A"), 0)
        answer.setCurrentIndex(answer_index)      
        self.cardTypes.setCellWidget(row, 2, answer)


        input_methods = ["Typing","Multiple-Choice", "Tapping"]
        inputMethod = QComboBox()
        inputMethod.addItems(input_methods)
        current_method = self.indexOf(input_methods, params.get("in"))
        inputMethod.setCurrentIndex(current_method)
        self.cardTypes.setCellWidget(row, 3, inputMethod)

        prompt = QLineEdit(params.get("prompt", ""))
        prompt_opacity = QGraphicsOpacityEffect()
        prompt_opacity.setOpacity(0.5)
        prompt.setGraphicsEffect(prompt_opacity)
        self.cardTypes.setCellWidget(row, 4, prompt)

        extra_options = ["ー"] + current_fields
        front_extra = QComboBox()
        front_extra.addItems(extra_options)
        extra_index = self.indexOf(extra_options, params.get("Extra"))
        front_extra.setCurrentIndex(extra_index)
        self.cardTypes.setCellWidget(row, 5, front_extra)        

        # Add remove button
        remove_button = QPushButton("-")
        remove_button.clicked.connect(self.remove_cardType)
        self.cardTypes.setCellWidget(row, self.cardTypes.columnCount()-2, remove_button)

        # Add clone button
        clone_button = QPushButton("↓+")
        clone_button.clicked.connect(self.clone_cardType)
        self.cardTypes.setCellWidget(row, self.cardTypes.columnCount()-1, clone_button)        

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
                tooltip(f'cloned row {r}')

                params = self.card_row2dic(r)
                # params.pop("Name", None)
                # params.pop("prompt", None)

                self.add_cardType(params)
                break        

    def remove_cardType(self):
        sender_button = self.sender()

        if self.cardTypes.rowCount() <= 1:
            return

        for r in range(self.cardTypes.rowCount()):
            if self.cardTypes.cellWidget(r, self.cardTypes.columnCount()-2) == sender_button:
                tooltip(f'removed row {r}')
                self.cardTypes.removeRow(r)
                break

    def get_preset_options(self):
        fields = [self.field_row2dic(r) for r in range(self.fieldsTable.rowCount())]
        card_types = [self.card_row2dic(r) for r in range(self.cardTypes.rowCount())]

        return {"Fields": fields, "Card Types": card_types}

    def get_full_options(self):
        options = self.get_preset_options()
        options["Note Type"] = self.noteType.text()
        options["Theme"] = self.theme.currentText()

        return options