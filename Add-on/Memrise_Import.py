from aqt.utils import tooltip

class MemriseImportSettings(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Import Memrise community courses")

        self.importProgress_toggle = QCheckBox()
        self.importProgress_toggle.setChecked(False)
        layout.addWidget(self.importProgress_toggle)

        # Ok/Cancel
        button_ok = QPushButton("Import")
        button_ok.clicked.connect(self.accept)
        button_cancel = QPushButton("Cancel")
        button_cancel.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
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