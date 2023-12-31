import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QPushButton, QLineEdit, QApplication


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700,500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(40, 40, 480, 320)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(40, 400, 480, 48)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(560, 400, 110, 48)

        self.show()


def main():
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
