'''
 Used Pyjokes And Pyttsx3 Module For This Simple Joker Program
'''

import pyttsx3, src
import pyfiglet
from colorama import Fore
import warnings
warnings.filterwarnings("ignore")


engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

styled_text=pyfiglet.figlet_format('JOKER',font= 'ansi_shadow')
print(Fore.RED + styled_text)
print("\033[1m\033[93mCreator\033[00m: \033[1m@VadaPavMan\033[0m")
print("\033[1m\033[93mGithub\033[00m: https://github.com/VadaPavMan")
input(Fore.WHITE + "\033[1m\nPress Enter To Start...\033[00m")

engine.say("My Name is Lisa, Im a Comedian \n i tell you I T related jokes in your preferred language")
engine.runAndWait()

engine.say("Which Language You Prefer ?")
engine.runAndWait()
lang = src.lang()

engine.say("Here Is A Joke")
engine.runAndWait()
src.jokes(lang)
src.operation(lang)

engine.stop()
