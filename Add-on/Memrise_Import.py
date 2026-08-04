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

from aqt.utils import tooltip
from aqt.qt import *
from PyQt6 import QtCore, QtWidgets

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
        headerMaster.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Fixed)
        headerMaster.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Fixed)

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

        # multiple choice filling
        self.choices_drop = QComboBox()
        self.choices_drop.addItems(["leave empty", "import", "autofill", "autofill empty"])
        self.choices_drop.setCurrentIndex(1)

        # reverse tests
        self.reverse_drop = QComboBox()
        self.reverse_drop.addItems(["auto", "all", "none", "flagged", "exclude flagged"])
        self.reverse_drop.setCurrentIndex(0)

        # decks group
        self.subdecks_checkbox = QCheckBox()
        self.subdecks_checkbox.setChecked(True)
        self.levels_checkbox = QCheckBox()
        self.levels_checkbox.setChecked(True)



        ## Layout

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(coursesLable)
        layout.addWidget(self.coursesTable)

        tests_group = QGroupBox("Test types")
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


        scheduling_row = QHBoxLayout()
        scheduling_row.addWidget(QLabel("Import Learning progress"))
        scheduling_row.addWidget(self.scheduling_checkbox)
        scheduling_row.addStretch()
        layout.addLayout(scheduling_row)

        # ▼ Advanced

        choices_row = QHBoxLayout()
        choices_row.addWidget(QLabel("Choices: "))
        choices_row.addWidget(self.choices_drop)
        choices_row.addStretch()
        layout.addLayout(choices_row)

        reverse_row = QHBoxLayout()
        reverse_row.addWidget(QLabel("Reverse Cards: "))
        reverse_row.addWidget(self.reverse_drop)
        reverse_row.addStretch()
        layout.addLayout(reverse_row)


        subdecks_group = QGroupBox("Subdecks")
        subdecks_layout = QVBoxLayout()
        subdecks_group.setLayout(subdecks_layout)
        layout.addWidget(subdecks_group)

        subdeck_row = QHBoxLayout()
        subdeck_row.addWidget(QLabel("Replicate folder tree"))
        subdeck_row.addWidget(self.subdecks_checkbox)
        subdeck_row.addStretch()
        subdecks_layout.addLayout(subdeck_row)

        levels_row = QHBoxLayout()
        levels_row.addWidget(QLabel("Subdecks from levels"))
        levels_row.addWidget(self.levels_checkbox)
        levels_row.addStretch()
        subdecks_layout.addLayout(levels_row)


#############################

        # Ok/Cancel + Help
        button_help = QPushButton("Help")
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

def import_courses():
    dialog = MemriseImportSettings()
    if not dialog.exec():
        return
    import_options = dialog.get_full_options()

    tooltip(import_options["importProgress"])