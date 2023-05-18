import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QHBoxLayout, \
                            QLineEdit, QLabel, QMainWindow, QMessageBox,     \
                            QPushButton, QTextEdit, QVBoxLayout, QWidget


class FileInputDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        self.file_label = QLabel("Please choose a .csv file or drop it here", self)
        self.file_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.file_label)

        self.file_lineedit = QLineEdit(self)
        self.layout.addWidget(self.file_lineedit)

        self.button_layout = QHBoxLayout()  # Use QHBoxLayout for buttons
        self.file_button = QPushButton("Browse", self)
        self.file_button.clicked.connect(self.browse_file)
        self.button_layout.addWidget(self.file_button)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.open_output_dialog)
        self.button_layout.addWidget(self.submit_button)

        self.layout.addLayout(self.button_layout)  # Add the button layout to the main layout

        self.setLayout(self.layout)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv)")  # Specify file filter
        if file_path:
            self.file_lineedit.setText(file_path)
        else:
            self.show_error_dialog("No file selected!")

    def open_output_dialog(self):
        file_path = self.file_lineedit.text()
        if file_path.endswith(".csv"):
            output_dialog = FileOutputDialog(file_path)
            output_dialog.exec_()
        else:
            self.show_error_dialog("Invalid file format!")

    def show_error_dialog(self, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.exec_()


class FileOutputDialog(QDialog): 
    def __init__(self, file_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Email Validity Result")
        self.setModal(True)  

        self.layout = QVBoxLayout(self)

        self.file_textedit = QTextEdit(self)
        self.file_textedit.setReadOnly(True)
        self.layout.addWidget(self.file_textedit)

        with open(file_path, "r") as file:
            file_content = file.read()
            self.file_textedit.setText(file_content)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Validator")
        self.setGeometry(500, 500, 1000, 750)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignCenter)

        self.file_input_widget = FileInputDialog(self.central_widget)
        self.layout.addWidget(self.file_input_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
