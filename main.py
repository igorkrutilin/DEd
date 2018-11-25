from kivy.config import Config
Config.set("graphics", "width", 500)
Config.set("graphics", "height", 500)

import datetime
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def get_date():
    today = datetime.date.today()
    """
    ususally I write my diary at night so just getting current date and placing it as file name is incorrect
    so we need to check current time and if it's less than 12 (maybe I'll write diary next day morning) we say,
    that date we need is yesterday
    """
    if datetime.datetime.now().hour < 12:
        date = today - datetime.timedelta(days = 1)
    else:
        date = today
    date = date.strftime("%d.%m.%Y")
    return date

text = ""

def create_file(instance):
    global text
    name_of_file = get_date() + ".txt"
    file = open("./Дневник/" + name_of_file, "w", encoding="utf-8")
    file.write(text)
    file.close()

def on_text(instance, value):
    global text
    text = value

class DEdApp(App):
    def build(self):
        layout = FloatLayout(size = (500, 500))
        editor = TextInput(text="")
        editor.bind(text = on_text)
        layout.add_widget(editor)
        save_button = Button(
            text = "Save",
            font_size = "15",
            size_hint = (.2, .1),
            pos = (500 - 120, 20)
        )
        global text
        text = editor.text
        save_button.bind(on_press = create_file)
        layout.add_widget(save_button)
        return layout

if __name__ == "__main__":
    DiaryApp().run()
