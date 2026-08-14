# This script is part of the Lt-Cards Add-on for Anki.
# Source: github.com/Eltaurus-Lt/Anki-Card-Templates
# 
# Copyright © 2026 Eltaurus
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

from aqt import mw
from aqt.qt import *
from PyQt6 import QtCore, QtWidgets

class NoScrollComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()

class QBatchDialog(QFileDialog):
    def __init__(self, caption="Select File or Folder", directory="", filter="All Files (*)"):
        global import_folder
        super().__init__(mw)

        self.setWindowTitle(caption)

        if directory and os.path.exists(directory):
            self.setDirectory(directory)
        else:
            self.setDirectory(os.path.expanduser("~"))
            
        filters = filter.split(";;") if ";;" in filter else [filter]
        self.setNameFilters(filters)
        
        self.setOption(QFileDialog.Option.DontUseNativeDialog, True)
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        
        # self.btn_enter = QPushButton("Open Folder", self)
        # self.btn_enter.clicked.connect(self.enter_selected_folder)
        self.btn_import = QPushButton("Import", self)

        self.file_view = self.findChild(QListView, "listView")
        self.tree_view = self.findChild(QTreeView, "treeView")
                    
        if self.file_view:
            self.file_view.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        if self.tree_view:
            self.tree_view.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)


        # modify layout
        if type_label := self.findChild(QLabel, "fileTypeLabel"): type_label.hide()
        if type_combo := self.findChild(QComboBox, "fileTypeCombo"): type_combo.hide()
        name_label = self.findChild(QLabel, "fileNameLabel")
        self.name_input = self.findChild(QLineEdit, "fileNameEdit")
        button_box = self.findChild(QDialogButtonBox)
        if button_box:
            ok_button = button_box.button(QDialogButtonBox.StandardButton.Open)
            cancel_button = button_box.button(QDialogButtonBox.StandardButton.Cancel)
            button_box.hide()
            self.btn_import.clicked.connect(lambda *_: self.confirm_import())
        
        new_row = QWidget()
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)
        new_row.setLayout(row_layout)

        if name_label: 
            name_label.setText("Selected: ")
            name_label.adjustSize()
        if self.name_input:
            self.name_input.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        # row_layout.addWidget(self.btn_enter)
        # self.btn_enter.hide()
        row_layout.addWidget(self.btn_import)
        if cancel_button:
            row_layout.addWidget(cancel_button)


        grid = self.findChild(QGridLayout)
        if grid:
            grid.addWidget(name_label, 2, 0)
            grid.addWidget(self.name_input, 2, 1)
            grid.addWidget(new_row, 2, 2)


        for view in (self.file_view, self.tree_view):
            if view and view.selectionModel():
                view.selectionModel().selectionChanged.connect(lambda *_: self.update_ui_state())
        self.directoryEntered.connect(lambda *_: self.update_ui_state())


    def update_ui_state(self):
        selected = self.selectedFiles()
        if selected:
            self.name_input.setText(", ".join([os.path.basename(p) for p in selected]))
            # if len(selected) > 1:
            #     self.btn_import.setText(f"Import ({len(selected)} sources)")
            # elif os.path.isdir(selected[0]):
            #     self.btn_import.setText("Import Folder")
            # else:
            #     self.btn_import.setText("Import File")
        else:
            self.name_input.setText(os.path.basename(self.directory().absolutePath()))
            # self.btn_import.setText("Import Folder")

    def confirm_import(self):
        global import_folder
        import_folder = self.directory().absolutePath()
        if self.name_input.text():
            QtWidgets.QDialog.done(self, QtWidgets.QDialog.DialogCode.Accepted)


    def selectedFiles(self):
        for view in (self.file_view, self.tree_view):
            if view and view.selectionModel() and view.selectionModel().hasSelection():
                return super().selectedFiles()

        return [self.directory().absolutePath()]