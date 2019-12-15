from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainoperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainoperatorApp(App):
    def build(self):
        return MainoperatorWindow()


if __name__ == "__main__":
    op = MainoperatorApp()
    op.run()
