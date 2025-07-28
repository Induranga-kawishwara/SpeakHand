from kivymd.uix.screen import MDScreen
from ProjectFiles.applibs import utils
import warnings

# Load the corresponding KV file
utils.load_kv("Alphabet.kv")

# Suppress warnings
warnings.filterwarnings('ignore')

# Define the Alphabet screen
class Alphabet_Screen(MDScreen):
    pass
