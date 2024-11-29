from app.views.login import LoginView
from app.config import Configs

class LoginController:
    def __init__(self):
        self.view = LoginView()
        self.view.button.clicked.connect(self.login)

    def show(self):
        self.view.show()

    def login(self):
        print(f'Username: {self.view.input1.text()}, Password: {self.view.input2.text()}')
        print(f'Base url: {Configs.BASE_URL}')