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

import os, webbrowser

from aqt import mw
from aqt.qt import *
from PyQt6 import QtCore, QtWidgets, QtGui

from .py_utils import user_files


addons_folder = mw.addonManager.addonsFolder()
addon_name = mw.addonManager.addonFromModule(__name__)
addon_path = os.path.join(addons_folder, addon_name)

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


    def __init__(self):
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
        self.coursesTable.setColumnWidth(1, int(5 * lh))
        self.coursesTable.setColumnWidth(2, int(7 * lh))
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


        importOptions_group = QGroupBox("Imported data")
        importOptions_layout = QVBoxLayout()
        importOptions_group.setLayout(importOptions_layout)
        layout.addWidget(importOptions_group)

        data_row = QHBoxLayout()
        data_row.addWidget(QLabel("Learning progress")) 
        data_row.addWidget(self.scheduling_checkbox)
        data_row.addSpacing(2 * lh)
        data_row.addWidget(QLabel("Media"))
        data_row.addWidget(self.media_checkbox)
        data_row.addSpacing(2 * lh)
        data_row.addWidget(QLabel("Metadata")) # description, thumbnails
        data_row.addWidget(self.meta_checkbox)
        data_row.addStretch()
        importOptions_layout.addLayout(data_row)


        tests_group = QGroupBox("Testing")
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
        tests_row2.addSpacing(2 * lh)
        tests_row2.addWidget(QLabel("Multiple Choice"))
        tests_row2.addWidget(self.multichoiceTests_checkbox)
        tests_row2.addSpacing(2 * lh)
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


        self.add_courseRow("course1")
        self.add_courseRow("path2")

def import_courses():
    dialog = MemriseImportSettings()
    if not dialog.exec():
        return
    import_options = dialog.get_full_options()

    mw.reviewer.web.eval(f'console.log(`{import_options["importProgress"]}`)')