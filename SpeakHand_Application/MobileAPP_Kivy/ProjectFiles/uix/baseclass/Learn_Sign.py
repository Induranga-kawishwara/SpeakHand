from ProjectFiles.applibs import utils
from kivymd.uix.screen import MDScreen
import warnings

utils.load_kv("Learn_Sign.kv")
warnings.filterwarnings('ignore')

class Learn_Sign_Screen(MDScreen):
    pass