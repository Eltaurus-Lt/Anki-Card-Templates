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

import os, re, webbrowser

from aqt import mw
from aqt.qt import *
from PyQt6 import QtCore, QtWidgets, QtGui
from aqt.utils import tooltip

from .py_utils import user_files


addons_folder = mw.addonManager.addonsFolder()
addon_name = mw.addonManager.addonFromModule(__name__)
addon_path = os.path.join(addons_folder, addon_name)
import_folder = os.path.expanduser("~/Downloads")

# move to utils
def indexOf( array, el, default = 0):
        try:
            return array.index(el)
        except ValueError:
            return default

# move to user_files
def getThemeList():
    themeList = user_files.list("Color Themes", ".css")
    themeList.insert(0, "ー")
    default = indexOf(themeList, "Memrise", indexOf(themeList, "Anki", 1))
    return themeList, default


class NoScrollComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()


# move to Dialogs.py
class QFolderOrFileDialog(QFileDialog):
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



class MemriseImportSettings(QDialog):
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

    def add_courseRow(self, path):
        row = self.coursesTable.rowCount()
        self.coursesTable.setRowCount(row + 1)

        course = QLabel(path)
        self.coursesTable.setCellWidget(row, 0, course)

        theme_drop = NoScrollComboBox() 
        themeList, defaultIndex = getThemeList()
        theme_drop.addItems(themeList)
        theme_drop.setCurrentIndex(defaultIndex)
        self.coursesTable.setCellWidget(row, 1, theme_drop)

        noteType_drop = NoScrollComboBox()
        noteType_drop.addItems([f"(auto {n})" for n in range(3)])
        noteType_drop.insertSeparator(noteType_drop.count())
        noteType_drop.addItems([m["name"] for m in mw.col.models.all()])
        noteType_drop.setCurrentIndex(1)
        self.coursesTable.setCellWidget(row, 2, noteType_drop)

        import_checkbox = QCheckBox()
        import_checkbox.setChecked(True)
        checkbox_cell = QWidget()
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_cell.setLayout(checkbox_layout)
        checkbox_layout.addWidget(import_checkbox)
        self.coursesTable.setCellWidget(row, 3, checkbox_cell)


    def __init__(self, courses):
        super().__init__()

        self.setStyleSheet("""
            QHeaderView::section:horizontal { padding: 0; }
            QHeaderView::section:vertical { padding: 7px; }
            QTableCornerButton::section { background: #febd11; }
            QTableWidget::item {  }
            QCheckBox { padding-left: 7px; }
            QToolTip {  }
            QHeaderView::section { 
                color: #29374a; 
                background: #febd11; 
                font-weight: bold; 
                font-size: 15px; 
            }
        """)

        self.tableButtonStyleSheet = """
            QPushButton {
                padding-left: 0px;
                padding-right: 0px;
            }
        """



        ## Widgets

        self.setWindowTitle("Memrise Course Import")
        self.setWindowIcon(QtGui.QIcon(os.path.join(addon_path, "icons", "import.ico")))
        coursesLable = QLabel("Courses")
        font_metrics = QFontMetrics(coursesLable.font())
        lh = font_metrics.lineSpacing()
        self.setMinimumWidth(36 * lh)

        # Main table
        self.coursesTable = QTableWidget(0, 4)
        self.setHeadersWithTooltips(self.coursesTable, [
            ("Course", None),
            ("Theme", None),
            ("Note Type", None),
            ("Import", None)])
        self.coursesTable.horizontalHeader().setMinimumSectionSize(2 * lh)
        self.coursesTable.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.NoSelection)
        self.coursesTable.cellClicked.connect(lambda r, c: self.toggleCellCheckbox(self.coursesTable.cellWidget(r, c)))
        self.coursesTable.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.coursesTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.coursesTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)


        headerMaster = self.coursesTable.horizontalHeader()
        self.coursesTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        headerMaster.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.coursesTable.setColumnWidth(1, int(6 * lh))
        self.coursesTable.setColumnWidth(2, int(6 * lh))
        self.coursesTable.setColumnWidth(3, int(3.5 * lh))
        headerMaster.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Fixed)
        headerMaster.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Interactive)
        headerMaster.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Fixed)
        headerMaster.setMinimumSectionSize(3 * lh)
        headerMaster.setMaximumSectionSize(15 * lh)

        # tests group
        self.audioTests_checkbox = QCheckBox()
        self.audioTests_checkbox.setChecked(True)
        self.typingTests_checkbox = QCheckBox()
        self.typingTests_checkbox.setChecked(True)
        self.multichoiceTests_checkbox = QCheckBox()
        self.multichoiceTests_checkbox.setChecked(True)
        self.tappingTests_checkbox = QCheckBox()
        self.tappingTests_checkbox.setChecked(False)

        self.scheduling_checkbox = QCheckBox()
        self.scheduling_checkbox.setChecked(True)
        self.media_checkbox = QCheckBox()
        self.media_checkbox.setChecked(True)
        self.meta_checkbox = QCheckBox()
        self.meta_checkbox.setChecked(True)

        # multiple choice filling
        self.choices_drop = QComboBox()
        self.choices_drop.addItems(["Leave empty", "Import", "Autofill", "Autofill empty"])
        self.choices_drop.setCurrentIndex(1)

        # reverse tests
        self.reverse_drop = QComboBox()
        self.reverse_drop.addItems(["Auto", "All", "None", "Flagged", "Exclude flagged"])
        self.reverse_drop.setCurrentIndex(0)

        # decks group
        self.subdecks_checkbox = QCheckBox()
        self.subdecks_checkbox.setChecked(True)
        self.levels_checkbox = QCheckBox()
        self.levels_checkbox.setChecked(True)



        ## Layout

        layout = QVBoxLayout()
        self.setLayout(layout)

        # layout.addWidget(coursesLable)
        layout.addWidget(self.coursesTable)


        importOptions_group = QGroupBox("Import:")
        importOptions_layout = QVBoxLayout()
        importOptions_group.setLayout(importOptions_layout)
        layout.addWidget(importOptions_group)

        data_row = QHBoxLayout()
        data_row.addWidget(QLabel("Learning progress")) 
        data_row.addWidget(self.scheduling_checkbox)
        data_row.addSpacing(1 * lh)
        data_row.addWidget(QLabel("Media"))
        data_row.addWidget(self.media_checkbox)
        data_row.addSpacing(1 * lh)
        data_row.addWidget(QLabel("Metadata")) # description, thumbnails
        data_row.addWidget(self.meta_checkbox)
        data_row.addStretch()
        importOptions_layout.addLayout(data_row)


        tests_group = QGroupBox("Tests")
        # todo tooltip : at least 1 typing-tapping should be enabled, applicable to newly created note types only
        tests_layout = QVBoxLayout()
        tests_group.setLayout(tests_layout)
        layout.addWidget(tests_group)

        tests_row1 = QHBoxLayout()
        tests_row1.addWidget(QLabel("Audio"))
        tests_row1.addWidget(self.audioTests_checkbox)
        tests_row1.addStretch()
        tests_layout.addLayout(tests_row1)

        tests_row2 = QHBoxLayout()
        tests_row2.addWidget(QLabel("Typing"))
        tests_row2.addWidget(self.typingTests_checkbox)
        tests_row2.addSpacing(1 * lh)
        tests_row2.addWidget(QLabel("Multiple Choice"))
        tests_row2.addWidget(self.multichoiceTests_checkbox)
        tests_row2.addSpacing(1 * lh)
        tests_row2.addWidget(QLabel("Tapping"))
        tests_row2.addWidget(self.tappingTests_checkbox)
        tests_row2.addStretch()
        tests_layout.addLayout(tests_row2)

        # ▼ Advanced

        # choices_row = QHBoxLayout()
        # choices_row.addWidget(QLabel("Choices: "))
        # choices_row.addWidget(self.choices_drop)
        # choices_row.addStretch()
        # layout.addLayout(choices_row)

        # reverse_row = QHBoxLayout()
        # reverse_row.addWidget(QLabel("Reverse Cards: "))
        # reverse_row.addWidget(self.reverse_drop)
        # reverse_row.addStretch()
        # layout.addLayout(reverse_row)


        # subdecks_group = QGroupBox("Subdecks")
        # subdecks_layout = QVBoxLayout()
        # subdecks_group.setLayout(subdecks_layout)
        # layout.addWidget(subdecks_group)

        # subdeck_row = QHBoxLayout()
        # subdeck_row.addWidget(QLabel("Replicate folder tree"))
        # subdeck_row.addWidget(self.subdecks_checkbox)
        # subdeck_row.addStretch()
        # subdecks_layout.addLayout(subdeck_row)

        # levels_row = QHBoxLayout()
        # levels_row.addWidget(QLabel("Subdecks from levels"))
        # levels_row.addWidget(self.levels_checkbox)
        # levels_row.addStretch()
        # subdecks_layout.addLayout(levels_row)

        # Ok/Cancel + Help
        button_help = QPushButton("Help")
        button_help.clicked.connect(lambda: webbrowser.open("https://forums.ankiweb.net/t/memrise-card-template-support-thread"))
        button_ok = QPushButton("Import")
        button_ok.clicked.connect(self.accept)
        button_cancel = QPushButton("Cancel")
        button_cancel.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button_help)
        button_layout.addStretch()
        button_layout.addWidget(button_ok)
        button_layout.addWidget(button_cancel)

        layout.addLayout(button_layout)


        # populate courses table
        for course in courses:
            self.add_courseRow(f"{"::".join([*course["deck tree"], course["proper name"]])} [{course["id"]}]")


def courseScan(root_path):
    def shortTab(csv_filename):
        match = re.match(r"^(.+)\[(\d+)\](?:_\((?:~?\d+|\d+ of \d+)\))?\.csv$", csv_filename)
        return (match.group(1).strip(), match.group(2)) if match else False

    def fullTab(short_tab, full_path):
        global import_folder

        rel_path = os.path.relpath(full_path, import_folder).split(os.sep)

        deck_tree = rel_path[:-1]

        if len(deck_tree) > 0 and deck_tree[-1].startswith(short_tab[0]):
            deck_tree.pop()

        return {
                "proper name": short_tab[0],
                "id": short_tab[1],
                "deck tree": deck_tree,
                "csv path": full_path
                }

    if os.path.isdir(root_path):
        course_tabs = []
        for root, _, files in os.walk(root_path):
            for f in files:
                if short_tab := shortTab(f):
                    course_tabs.append((short_tab, os.path.join(root, f)))
        return [fullTab(*course_tab) for course_tab in course_tabs]
    elif os.path.isfile(root_path) and (short_tab := shortTab(os.path.basename(root_path))):
        return [fullTab(short_tab, root_path)]

    return []


def import_courses():

    ## File Selection Dialog
    global import_folder
    file_dialog = QFolderOrFileDialog(
        caption = "Select course .csv files, course folders, or a parent folder with multiple courses",
        directory = import_folder,
        filter = "CSV Files (*.csv);;All Files (*)"
        )

    if file_dialog.exec():
        selected_paths = file_dialog.selectedFiles()
        if not selected_paths:
            return
    else:
        return

    courses = [course for path in selected_paths for course in courseScan(path)]

    if not courses:
        tooltip("No courses found in the selection")
        return

    ## Import Options Dialog
    dialog = MemriseImportSettings(courses)
    if not dialog.exec():
        return
    import_options = dialog.get_full_options()


    # mw.reviewer.web.eval(f'console.log(`{import_options["importProgress"]}`)')