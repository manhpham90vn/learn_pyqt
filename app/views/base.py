import os
import sys

from PySide6.QtWidgets import QWidget


class BaseView(QWidget):

    def getPath(self):
        if getattr(sys, 'frozen', False):
            return sys._MEIPASS
        else:
            return os.getcwd()

    def setStyle(self, path):
        with open(os.path.join(self.getPath(), path), "r") as file:
            self.setStyleSheet(file.read())
