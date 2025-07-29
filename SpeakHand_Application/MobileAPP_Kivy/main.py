from kivy.utils import platform

# Configure window size for desktop testing
if platform != 'android':
    from kivy.config import Config
    Config.set("graphics", "width", "360")
    Config.set("graphics", "height", "740")
    Config.set("graphics", "borderless", "True")

from kivy.core.window import Window
Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

# Import your screens
from ProjectFiles.uix.baseclass.Main_Menu import Main_Menu_Screen
from ProjectFiles.uix.baseclass.Sign_to_text import Sign_to_text_Screen
from ProjectFiles.uix.baseclass.Text_to_Sign import Text_to_Sign_Screen
from ProjectFiles.uix.baseclass.Text_to_Speech import Text_to_Speech_Screen
from ProjectFiles.uix.baseclass.Learn_Sign import Learn_Sign_Screen
from ProjectFiles.uix.baseclass.Alphabet import Alphabet_Screen

class SpeakHandApp(MDApp):
    def build(self):
        # Set basic theme
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        sm = ScreenManager()
        sm.add_widget(Main_Menu_Screen(name="main_menu"))
        sm.add_widget(Sign_to_text_Screen(name="sign_to_text"))
        sm.add_widget(Text_to_Sign_Screen(name="text_to_sign"))
        sm.add_widget(Text_to_Speech_Screen(name="text_to_speech"))
        sm.add_widget(Learn_Sign_Screen(name="learn_sign"))
        sm.add_widget(Alphabet_Screen(name="alphabet"))

        return sm

if __name__ == "__main__":
    SpeakHandApp().run()
