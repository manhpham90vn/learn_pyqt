import sys
from .views.login import Login
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()