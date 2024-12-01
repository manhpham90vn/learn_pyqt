from PySide6.QtCore import QSettings


class Configs:
    _instance = None
    _singleton = None

    BASE_URL = 'https://api.github.com'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._settings = QSettings("MyApp", "MyOrganization")
        return cls._instance

    @property
    def settings(self):
        return self._settings
