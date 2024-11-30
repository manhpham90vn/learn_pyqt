from PyQt6.QtWidgets import ( QWidget, QPushButton, QLabel, QLineEdit, 
                             QGridLayout, QSpacerItem, QSizePolicy, 
                             QHBoxLayout, QGridLayout, QVBoxLayout
                             )
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from app.views.base import BaseView
import os
import sys

class MainView(BaseView):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 300)
        self.setWindowTitle("Main")
        self.setWindowIcon(QIcon(os.path.join(self.getPath(), "assets", "images", "icon.png")))
        self.setContentsMargins(10, 10, 10, 10)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.label = QLabel("Welcome to Main")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label, 0, 0, 1, 2)
        
        self.button = QPushButton("Logout")
        self.button.setFixedWidth(150)
        layout.addWidget(self.button, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        
        