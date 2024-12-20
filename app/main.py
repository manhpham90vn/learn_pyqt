import sys

from PySide6.QtWidgets import QApplication

from app.config import Configs
from app.controllers.login import LoginController
from app.controllers.main import MainController


def main():
    app = QApplication(sys.argv)
    settings = Configs().settings
    isLogin = settings.value('isLogin')

    if isLogin:
        main = MainController()
        main.show()
    else:
        loginController = LoginController()
        loginController.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
