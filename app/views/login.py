from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import os
import sys

class LoginView(QWidget):

    def getPath(self):
        if getattr(sys, 'frozen', False):
            return sys._MEIPASS
        else:
            return os.getcwd()

    def __init__(self):
        super().__init__()

        self.resize(400, 200)
        self.setWindowTitle("Login Form")
        self.setWindowIcon(QIcon(os.path.join(self.getPath(), "app", "assets", "images", "icon.png")))
        self.setContentsMargins(20, 20, 20, 20)
        
        layout = QGridLayout()
        self.setLayout(layout)

        self.label1 = QLabel("Name:")
        layout.addWidget(self.label1, 0, 0)

        self.label2 = QLabel("Password:")
        layout.addWidget(self.label2, 1, 0)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1, 0, 1)

        self.input2 = QLineEdit()
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input2, 1, 1)

        self.button = QPushButton("Login")
        self.button.setFixedWidth(150)
        layout.addWidget(self.button, 2, 1, Qt.AlignmentFlag.AlignCenter)

        with open(os.path.join(self.getPath(), "app", "assets", "styles", "login.css"), "r") as file:
            self.setStyleSheet(file.read())