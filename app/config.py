class Configs:
  _instance = None

  BASE_URL = 'https://api.github.com'

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance