from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.pickers import MDTimePicker
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_string('''
<Time>:
    MDRaisedButton:
        text: "Открыть выбор времени"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_release: root.open_time_picker()

    MDLabel:
        id: select_time
        text: "Тут время"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
''')

class Time(FloatLayout):
    select_time = ObjectProperty(None)

    def open_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        time_dialog.open()

    def on_save(self, instance, value):
        # Форматирование времени без секунд
        time_str = value.strftime("%H:%M")
        self.ids.select_time.text = time_str

    def on_cancel(self, instance):
        self.ids.select_time.text = "Время не выбрано"

from kivymd.app import MDApp

class TestApp(MDApp):
    def build(self):
        return Time()

if __name__ == '__main__':
    TestApp().run()