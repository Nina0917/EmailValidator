

import csv
import sys
import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QHBoxLayout, \
                            QLineEdit, QLabel, QMainWindow, QMessageBox,     \
                            QPushButton, QTableWidgetItem, QVBoxLayout, QWidget, \
                            QTableWidget, QComboBox
from utils.syntax_checker import SyntaxCheck
from utils.mx_checker import MXCheck
from utils.smtp_checker import check_email_smtp
from utils.disposable_checker import DisposableEmailChecker

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
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv)")
        if file_path:
            self.file_lineedit.setText(file_path)
        else:
            self.show_error_dialog("No file selected!")

    def open_output_dialog(self):
        file_path = self.file_lineedit.text()
        if file_path.endswith(".csv"):
            chunk_size = 2 
            data = read_csv_to_dict(file_path)
            chunks = [dict(list(data.items())[i:i+chunk_size]) for i in range(0, len(data), chunk_size)]

            results = {}
            lock = threading.Lock()
            threads = []

            for chunk in chunks:
                thread = threading.Thread(target=process_chunk, args=(chunk, results, lock))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

            output_dialog = FileOutputDialog(results)
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


def read_csv_to_dict(file_path):
    dictionary = {}
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                dictionary[row[0]] = False
    return dictionary

def validate_email(email):
    """
    validate_email:
    this method is a helper function of process chunk to check the validation of the email.
    input: email address
    output: Boolean
    """

    if not SyntaxCheck(email):
        return False
    elif not DisposableEmailChecker().is_disposable(email):
        return False
    elif not MXCheck(email):
        return False
    elif not check_email_smtp(email):
        return False
    else:
        return True

def process_chunk(data, results, lock):
    chunk_results = {}
    for email in data.keys():
        chunk_results[email] = validate_email(email)
    with lock:
        results.update(chunk_results)


class FileOutputDialog(QDialog):
    def __init__(self, dictionary, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Validation Results")
        self.setModal(True)
        self.setMinimumSize(1106, 800)

        self.layout = QVBoxLayout(self)

        self.filter_layout = QHBoxLayout()
        self.filter_label = QLabel("Filter by Validity:", self)
        self.filter_layout.addWidget(self.filter_label)

        self.filter_combobox = QComboBox(self)
        self.filter_combobox.addItem("All")
        self.filter_combobox.addItem("True")
        self.filter_combobox.addItem("False")
        self.filter_combobox.currentIndexChanged.connect(self.filter_table)
        self.filter_layout.addWidget(self.filter_combobox)

        self.layout.addLayout(self.filter_layout)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Email", "Validity"])
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table_widget.setColumnWidth(0, self.table_widget.columnWidth(0) * 2)

        self.populate_table(dictionary)

        self.layout.addWidget(self.table_widget)

        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_file)
        self.button_layout.addWidget(self.save_button)

        self.layout.addLayout(self.button_layout)

        self.filtered_dictionary = dictionary.copy()

    def populate_table(self, dictionary):
        row_count = 0
        for key, value in dictionary.items():
            self.table_widget.insertRow(row_count)
            key_item = QTableWidgetItem(key)
            value_item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row_count, 0, key_item)
            self.table_widget.setItem(row_count, 1, value_item)
            row_count += 1

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, "w") as file:
                writer = csv.writer(file)
                for row in range(self.table_widget.rowCount()):
                    key_item = self.table_widget.item(row, 0)
                    value_item = self.table_widget.item(row, 1)
                    writer.writerow([key_item.text(), value_item.text()])
            QMessageBox.information(self, "File Saved", "File saved successfully!")
        else:
            QMessageBox.warning(self, "Save File", "No file path specified!")

    def filter_table(self):
        selected_value = self.filter_combobox.currentText()
        self.table_widget.setRowCount(0) 
        row_count = 0
        for key, value in self.filtered_dictionary.items():
            if selected_value == "All" or (selected_value == "True" and value) or (selected_value == "False" and not value):
                self.table_widget.insertRow(row_count)
                key_item = QTableWidgetItem(key)
                value_item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row_count, 0, key_item)
                self.table_widget.setItem(row_count, 1, value_item)
                row_count += 1


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
