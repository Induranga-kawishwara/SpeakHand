from ProjectFiles.applibs import utils
from kivymd.uix.screen import MDScreen
import warnings

utils.load_kv("Alphabet.kv")
warnings.filterwarnings('ignore')

class Alphabet_Screen(MDScreen):
    pass