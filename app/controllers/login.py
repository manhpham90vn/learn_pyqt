from app.views.login import LoginView
from app.config import Configs
from app.controllers.base import BaseController

class LoginController(BaseController):
    def __init__(self):
        super().__init__(LoginView, 'app/assets/styles/login.css')
        self.view.button.clicked.connect(self.login)

    def login(self):
        print(f'Username: {self.view.input1.text()}, Password: {self.view.input2.text()}')
        print(f'Base url: {Configs.BASE_URL}')