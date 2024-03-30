from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


if __name__ == "__main__":
    DynamicLabelsApp().run()
