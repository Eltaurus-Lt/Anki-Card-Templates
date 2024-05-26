from aqt.qt import *
from PyQt6 import QtCore, QtWidgets

from aqt.utils import tooltip

def indexOf(array, el, default = 0):
    try:
        return array.index(el)
    except ValueError:
        return default

def is_choice_string(string):
    return ("choice" in string or "Choice" in string)

def choices_field_index(array):
    for i, string in enumerate(array):
        if is_choice_string(string):
            return i
    return len(array)-1

class FillChoices(QDialog):
    def __init__(self, notes_fields):
        super().__init__()

        # Create widgets
        self.source_label = QLabel("Source Field")
        self.source_field = QComboBox()
        self.source_field.addItems([field for field in notes_fields if not is_choice_string(field)])

        self.choices_label = QLabel("Choices Field")
        self.choices_field = QComboBox()
        self.choices_field.addItems(notes_fields)
        self.choices_field.setCurrentIndex(choices_field_index(notes_fields))

        self.radio_label = QLabel("Action")
        self.radio_group = QButtonGroup()
        self.radio_append = QRadioButton("Append")
        self.radio_overwrite = QRadioButton("Overwrite")
        self.radio_group.addButton(self.radio_append)

        self.radio_group.addButton(self.radio_overwrite)
        self.radio_append.setChecked(True)

        self.button_ok = QPushButton("OK")
        self.button_cancel = QPushButton("Cancel")

        # Create layout
        font_size = int(self.source_label.font().pointSize())

        layout = QVBoxLayout()
        layout.addWidget(self.source_label)
        layout.addWidget(self.source_field)
        layout.addWidget(self.choices_label)
        layout.addWidget(self.choices_field)

        layout.addWidget(self.radio_label)
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio_append)
        radio_layout.addSpacing(1 * font_size)
        radio_layout.addWidget(self.radio_overwrite)
        radio_layout.addStretch()
        layout.addLayout(radio_layout)

        layout.addSpacing(2 * font_size)
        layout.addStretch()
  
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.button_ok)
        button_layout.addWidget(self.button_cancel)
        layout.addLayout(button_layout)

        # Set size limits
        self.setMinimumWidth(30 * font_size)
        self.setMaximumHeight(25 * font_size)
        self.setMaximumWidth(45 * font_size)

        # Set layout
        self.setLayout(layout)

        # Connect signals
        self.button_ok.clicked.connect(self.accept)
        self.button_cancel.clicked.connect(self.reject)

    def get_selected_options(self):
        return self.source_field.currentText(), self.choices_field.currentText(), self.radio_append.isChecked()


### 

# onhover tooltips
# initial window sizes/stretch table to full width
# columns styles: bold/transparent/widths/...
# narrow buttons/ center +field
# bold table headers + 'cards' top margin
# top table auto height


# remove .show ?
# refactor private/public variables


class NoteTypeDesigner(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Note Type Creator")

        self.noteType = QLineEdit("Memrise (Lτ) Note Type")
        self.noteType.setToolTip("Name of the created Note Type<br><i>e.g.</i> \"Memrise (Lτ) Japanese\"<br><sub>It is recommended to keep 'Memrise (Lτ)' at the start of the name for the future add-on versions to be able to track the respective note types</sub>")
        self.noteType.setAlignment(Qt.AlignmentFlag.AlignCenter)


        fields_label = QLabel("Fields")
        self.fields = QTableWidget()
        self.fields.setColumnCount(6)
        self.fields.setHorizontalHeaderLabels(["Field Label", "Show Bigger", "Show after tests", "Static Keys", "Random Keys", ""])

        self.addField_button = QPushButton("+")
        self.addField_button.clicked.connect(lambda: self.add_field({}))

        cardTypes_label = QLabel("Cards")
        self.cardTypes = QTableWidget()
        self.cardTypes.setColumnCount(8)
        self.cardTypes.setHorizontalHeaderLabels(["Card Type", "Question", "Answer", "Input", "Prompt", "Front Extra", "", ""])

        self.add_field({"Name": "Learnable"})
        self.add_field({"Name": "Definition"})
        self.add_field({"Name": "Audio"})
        self.add_cardType({"Name": "Translation", "prompt": "Type the correct translation"})       

        button_ok = QPushButton("OK")
        button_ok.clicked.connect(self.accept)
        button_cancel = QPushButton("Cancel")
        button_cancel.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(button_ok)
        button_layout.addWidget(button_cancel)

        layout = QVBoxLayout()
        layout.addWidget(self.noteType)        
        layout.addWidget(fields_label)        
        layout.addWidget(self.fields)
        layout.addWidget(self.addField_button)
        layout.addWidget(cardTypes_label)        
        layout.addWidget(self.cardTypes)
        layout.addLayout(button_layout)
        self.setLayout(layout)


        # Styling
        #self.fields.setShowGrid(False)
        self.cardTypes.setShowGrid(False)
        #self.cardTypes.setStyleSheet("QTableWidget { background-color: transparent; }")
        self.cardTypes.resizeColumnsToContents()

#        self.show()


    def field_row2dic(self, row):

        return {
            "Name": self.fields.cellWidget(row, 0).text(),
            "large": self.fields.cellWidget(row, 1).layout().itemAt(0).widget().isChecked(),
            "back": self.fields.cellWidget(row, 2).layout().itemAt(0).widget().isChecked(),
            "static": self.fields.cellWidget(row, 3).text(),
            "random": self.fields.cellWidget(row, 4).text(),
        }

    def add_field(self, params):
        row = self.fields.rowCount()
        self.fields.setRowCount(row + 1)

        field_name = params.get("Name", f"Field {row+1}")
        name = QLineEdit(field_name)
        self.fields.setCellWidget(row, 0, name)
        name.textChanged.connect(self.rename_field)

        large = QCheckBox()
        large.setChecked(params.get("large", False))
        checkbox_cell = QWidget()
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_cell.setLayout(checkbox_layout)
        checkbox_layout.addWidget(large)
        self.fields.setCellWidget(row, 1, checkbox_cell)

        back = QCheckBox()
        back.setChecked(params.get("back", True))
        checkbox_cell = QWidget()
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_cell.setLayout(checkbox_layout)
        checkbox_layout.addWidget(back)
        self.fields.setCellWidget(row, 2, checkbox_cell)

        static = QLineEdit(params.get("static", ""))
        self.fields.setCellWidget(row, 3, static)

        random = QLineEdit(params.get("random", ""))
        self.fields.setCellWidget(row, 4, random)

        # Add remove button
        remove_button = QPushButton("-")
        remove_button.clicked.connect(self.remove_field)
        self.fields.setCellWidget(row, self.fields.columnCount()-1, remove_button)

        # Add the respective item to qboxes for each card type
        for r in range(self.cardTypes.rowCount()):
            self.cardTypes.cellWidget(r, 1).addItem(field_name) #question
            self.cardTypes.cellWidget(r, 2).addItem(field_name) #answer
            self.cardTypes.cellWidget(r, 5).addItem(field_name) #extra

    def rename_field(self):
        sender_field = self.sender()

        for r in range(self.fields.rowCount()):
            if self.fields.cellWidget(r, 0) == sender_field:
                break
        new_name = self.fields.cellWidget(r, 0).text()

        # Rename the respective item in qboxes for each card type
        for rC in range(self.cardTypes.rowCount()):
            self.cardTypes.cellWidget(rC, 1).setItemText(r, new_name) #question
            self.cardTypes.cellWidget(rC, 2).setItemText(r, new_name) #question
            self.cardTypes.cellWidget(rC, 5).setItemText(r+1, new_name) #question

    def remove_field(self):
        sender_button = self.sender()

        if self.fields.rowCount() <= 2:
            return

        for r in range(self.fields.rowCount()):
            if self.fields.cellWidget(r, self.fields.columnCount()-1) == sender_button:
                break

        tooltip(f'removed row {r}')                
        self.fields.removeRow(r)

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

        current_fields = [self.fields.cellWidget(r, 0).text() for r in range(self.fields.rowCount())]

        question = QComboBox()
        question.addItems(current_fields)
        question_index = indexOf(current_fields, params.get("Q"), 1)
        question.setCurrentIndex(question_index)        
        self.cardTypes.setCellWidget(row, 1, question)

        answer = QComboBox()
        answer.addItems(current_fields)
        answer_index = indexOf(current_fields, params.get("A"), 0)
        answer.setCurrentIndex(answer_index)      
        self.cardTypes.setCellWidget(row, 2, answer)


        input_methods = ["Type-in","Multiple-Choice"]
        inputMethod = QComboBox()
        inputMethod.addItems(input_methods)
        current_method = indexOf(input_methods, params.get("in"))
        inputMethod.setCurrentIndex(current_method)
        self.cardTypes.setCellWidget(row, 3, inputMethod)

        prompt = QLineEdit(params.get("prompt", ""))
        self.cardTypes.setCellWidget(row, 4, prompt)

        extra_options = ["ー"] + current_fields
        front_extra = QComboBox()
        front_extra.addItems(extra_options)
        extra_index = indexOf(extra_options, params.get("Extra"))
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
                params.pop("Name", None)
                params.pop("prompt", None)

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

    def get_selected_options(self):

        fields = [self.field_row2dic(r) for r in range(self.fields.rowCount())]
        card_types = [self.card_row2dic(r) for r in range(self.cardTypes.rowCount())]

        return {"Note Type": self.noteType.text(), "Fields": fields, "Cart Types": card_types}
