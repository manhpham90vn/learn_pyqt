from app.views.main import MainView
from app.config import Configs
from app.controllers.base import BaseController

class MainController(BaseController):
    def __init__(self):
        super().__init__(MainView, 'assets/styles/main.css')
        self.view.button.clicked.connect(self.logout)
        self.loginController = None
        
    def logout(self):
        settings = Configs().settings
        settings.setValue('isLogin', None)
        self.view.close()
        from app.controllers.login import LoginController
        self.loginController = LoginController()
        self.loginController.show()