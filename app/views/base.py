from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import os
import sys

class BaseView(QWidget):

    def getPath(self):
        if getattr(sys, 'frozen', False):
            return sys._MEIPASS
        else:
            return os.getcwd()

    def setStyle(self, path):
        with open(os.path.join(self.getPath(), path), "r") as file:
            self.setStyleSheet(file.read())