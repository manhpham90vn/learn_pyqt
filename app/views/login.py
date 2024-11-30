from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from app.views.base import BaseView
import os
import sys

class LoginView(BaseView):
    def __init__(self):
        super().__init__()

        self.resize(400, 200)
        self.setWindowTitle("Login Form")
        self.setWindowIcon(QIcon(os.path.join(self.getPath(), "assets", "images", "icon.png")))
        self.setContentsMargins(10, 10, 10, 10)
        
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

        spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer, 2, 0, 1, 2)

        self.button = QPushButton("Login")
        self.button.setFixedWidth(150)
        layout.addWidget(self.button, 3, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)