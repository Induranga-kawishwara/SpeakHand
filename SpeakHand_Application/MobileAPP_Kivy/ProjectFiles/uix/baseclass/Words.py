from ProjectFiles.applibs import utils
from kivy.lang import Builder
from kivy.uix.video import Video
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

utils.load_kv("Words.kv")


class Words_Screen(MDScreen):
    def on_enter(self):
        # Ensure that the layout has been fully loaded before accessing children
        grid = self.ids.button_grid  # Accessing button_grid using the id defined in words.kv
        if grid:
            # Example: Access the first button (Monday button)
            first_button = grid.children[0]
            print(f"First button text: {first_button.text}")  # Just an example action

    def filter_buttons(self, search_text):
        grid = self.ids.button_grid  # Accessing button_grid
        if grid:
            # Filter the buttons based on the search text
            for button in grid.children:
                button_text = button.text.lower()
                if search_text.lower() in button_text:
                    button.disabled = False  # Show the button if it matches
                else:
                    button.disabled = True  # Hide the button if it doesn't match

    def open_frames_popup(self, label):
        # Sample method to open popup when a button is pressed
        content = BoxLayout(orientation='vertical')
        video = Video(source=f'{label}.mp4', state='play')
        content.add_widget(video)

        popup = Popup(title=label, content=content, size_hint=(0.8, 0.8))
        popup.open()

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("Words.kv")  # Load the KV file for the screen

    def on_start(self):
        # Example to demonstrate the filter functionality
        screen = self.root.ids.words_screen
        screen.filter_buttons("monday")  # You can test by typing "monday" in the search bar

# Run the app
if __name__ == '__main__':
    MyApp().run()