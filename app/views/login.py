import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QMessageBox,
                               QPushButton, QVBoxLayout)

from app.views.base import BaseView


class LoginView(BaseView):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 300)
        self.setWindowTitle("Login Form")
        self.setWindowIcon(
            QIcon(os.path.join(self.getPath(), "assets", "images", "icon.png")))
        self.setContentsMargins(10, 10, 10, 10)

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        hbox1 = QHBoxLayout()
        self.label1 = QLabel("Name:")
        hbox1.addWidget(self.label1)

        self.input1 = QLineEdit()
        self.input1.setFixedWidth(300)
        self.input1.setPlaceholderText("Enter your name")
        hbox1.addWidget(self.input1)

        hbox2 = QHBoxLayout()
        self.label2 = QLabel("Password:")
        hbox2.addWidget(self.label2)

        self.input2 = QLineEdit()
        self.input2.setFixedWidth(300)
        self.input2.setPlaceholderText("Enter your password")
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)
        hbox2.addWidget(self.input2)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.button = QPushButton("Login")
        self.button.setFixedWidth(150)
        vbox.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

    def showDialog(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(message)
        msg.exec()
