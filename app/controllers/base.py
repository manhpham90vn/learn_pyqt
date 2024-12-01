class BaseController:
    def __init__(self, viewClass, style):
        self.view = viewClass()
        self.view.setStyle(style)

    def show(self):
        self.view.show()