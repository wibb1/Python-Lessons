from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, \
    QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QToolBar, QStatusBar, QMessageBox
import sys
import sqlite3

global main_window


class DatabaseConnection():
    def __init__(self, database_file="database.db"):
        self.database_file = database_file

    def connect(self):
        connection = sqlite3.connect(self.database_file)
        return connection
    # def insert


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        self.setFixedWidth(405)
        self.setFixedHeight(600)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)

        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        edit_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        edit_student_action.triggered.connect(self.edit)
        file_menu_item.addAction(edit_student_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addActions([add_student_action, search_action])

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.table.cellClicked.connect(self.cell_clicked)

        self.load_data()

    def load_data(self):
        connection = DatabaseConnection().connect()
        result = list(connection.execute("SELECT id, name, course, mobile FROM students"))
        self.table.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for col_num, cell_data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))
        connection.close()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if not children:
            self.status_bar.addWidget(delete_button)
            self.status_bar.addWidget(edit_button)

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(selfself):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ["Astronomy", "Biology", "Math", "Physics"]
        self.course_name.setPlaceholderText("Course Name")
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.phone_number = QLineEdit()
        self.phone_number.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_number)

        add_button = QPushButton()
        add_button.setText("Add Student")
        add_button.clicked.connect(self.add_student)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        number = self.phone_number.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", (name, course, number))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        search_button = QPushButton()
        search_button.setText("Search")
        search_button.clicked.connect(self.search_student)
        layout.addWidget(search_button)

        self.setLayout(layout)

    def search_student(self):
        name = self.student_name.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        result = cursor.execute("SELECT name, course, mobile FROM students WHERE name = ?", (name,))
        rows = list(result)
        print(rows)
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            main_window.table.item(item.row(), 1).setSelected(True)
        cursor.close()
        connection.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        layout = QVBoxLayout()

        # Get selected data from the table
        index = main_window.table.currentRow()
        self.student_id = main_window.table.item(index, 0)
        self.student_name = main_window.table.item(index, 1).text()
        self.student_course = main_window.table.item(index, 2).text()
        self.student_phone = main_window.table.item(index, 3).text()

        self.student_name = QLineEdit(self.student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ["Astronomy", "Biology", "Math", "Physics"]
        self.course_name.setPlaceholderText("Course Name")
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(self.student_course)
        layout.addWidget(self.course_name)

        self.phone_number = QLineEdit(self.student_phone)
        self.phone_number.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_number)

        add_button = QPushButton()
        add_button.setText("Update Student")
        add_button.clicked.connect(self.edit_student)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def edit_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        number = self.phone_number.text()
        id = self.student_id.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?", (name, course, number, id))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")

        layout = QGridLayout()

        # Get selected data from the table
        index = main_window.table.currentRow()
        self.student_id = main_window.table.item(index, 0)
        student_name = main_window.table.item(index, 1).text()
        student_course = main_window.table.item(index, 2).text()
        student_phone = main_window.table.item(index, 3).text()

        confirmation = QLabel(
            f"Are you sure you want to delete the following student?\n{student_name} {student_course} {student_phone}")
        yes = QPushButton("Yes")
        yes.clicked.connect(self.delete_student)
        no = QPushButton("No")
        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

    def delete_student(self):
        id = self.student_id.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (id,))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

        self.close()

        confirmation = QMessageBox()
        confirmation.setWindowTitle("Success")
        confirmation.setText("Successfully deleted student")
        confirmation.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About this app")
        content = 'This is an app created as part of the "Python Mega Course" to learn about PyQt'
        self.setText(content)


def main():
    app = QApplication(sys.argv)
    global main_window
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
