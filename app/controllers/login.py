from app.config import Configs
from app.controllers.base import BaseController
from app.views.login import LoginView


class LoginController(BaseController):
    def __init__(self):
        super().__init__(LoginView, 'assets/styles/login.css')
        self.view.button.clicked.connect(self.login)
        self.main = None

    def login(self):
        name = self.view.input1.text()
        password = self.view.input2.text()

        if name == 'admin' and password == 'admin':
            self.view.showDialog('Success', 'Login successful')
            settings = Configs().settings
            settings.setValue('isLogin', True)
            self.view.close()
            from app.controllers.main import MainController
            self.main = MainController()
            self.main.show()
        else:
            self.view.showDialog('Error', 'Invalid credentials')
