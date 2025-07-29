from main_imports import MDScreen
from ProjectFiles.applibs import utils
import pyttsx3
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase

# Load the KV file
utils.load_kv("Text_to_Speech.kv")


# Define custom Tab class to avoid FactoryException
class Tab(MDBoxLayout, MDTabsBase):
    """Custom Tab Content for MDTabs"""
    pass


class Text_to_Speech_Screen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize TTS engine
        self.tts_engine = pyttsx3.init()
        # Set speech properties
        self.tts_engine.setProperty("rate", 150)  # Speed
        self.tts_engine.setProperty("volume", 1)  # Volume (0.0 to 1.0)

    def speak_text(self, lang):
        """Speak text based on selected language."""
        if lang == "en":
            user_input = self.ids.text_input_english.text.strip()
            voice_name = "english"
        elif lang == "si":
            user_input = self.ids.text_input_sinhala.text.strip()
            voice_name = "si"
        else:
            user_input = None

        if user_input:
            print(f"Speaking in {lang}: {user_input}")
            # Search for appropriate voice
            voices = self.tts_engine.getProperty("voices")
            selected_voice = None
            for voice in voices:
                if voice_name in voice.id.lower() or voice_name in voice.name.lower():
                    selected_voice = voice.id
                    break

            # Set voice if found
            if selected_voice:
                self.tts_engine.setProperty("voice", selected_voice)
            else:
                print(f"No specific {voice_name} voice found. Using default.")

            # Speak the text
            self.tts_engine.say(user_input)
            self.tts_engine.runAndWait()
        else:
            print("No text provided for Text-to-Speech")

    def on_stop(self):
        """Stop TTS engine when exiting the screen."""
        self.tts_engine.stop()
