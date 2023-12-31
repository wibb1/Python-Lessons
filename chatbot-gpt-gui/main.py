import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QPushButton, QLineEdit, QApplication

from backend import Chatbot

import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()
        self.setMinimumSize(700, 500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(40, 40, 480, 320)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(40, 400, 480, 48)
        self.input_field.returnPressed.connect(self.send_message)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(560, 400, 110, 48)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>User: {user_input}</p>")

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333'; backgroud-color:#e9e9e9>Chatbot: {response}</p>")


def main():
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
