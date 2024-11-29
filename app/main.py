import sys
from app.controllers.login import LoginController
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    loginController = LoginController()
    loginController.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()