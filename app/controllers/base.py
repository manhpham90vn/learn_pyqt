from app.views.login import LoginView
from app.config import Configs

class BaseController:
    def __init__(self, viewClass, style):
        self.view = viewClass()
        self.view.setStyle(style)

    def show(self):
        self.view.show()