'''
 Some Languages Are Not Supported, Will Add Them Later On
'''

import pyjokes, pyttsx3, random

engine = pyttsx3.init()
def jokes(lang):
    speak = pyttsx3.init()
    joke = pyjokes.get_joke(lang)
    speak.say(joke)
    print("\033[1m\n", joke, "\033[00m")
    speak.runAndWait()
    speak.stop()

def print_menu():
    print("\033[1m\033[93m\n1. Tell Me Another Joke.\n2. Change Language.\n3. Exit The Program.\033[00m")

def ask_again():
    ask = random.randint(1, 3)
    if(ask == 1):
        engine.say("Would You Like Me To Tell You Another One ?")
        engine.runAndWait()
    if(ask == 2):
        engine.say("Do You Want Me To Tell You Another Joke ?")
        engine.runAndWait()
    if(ask == 3):
        engine.say("I Have Another One\n Can I ?")
        engine.runAndWait()

def end():
    close = random.randint(1, 3)
    if(close == 1):
        engine.say("Goodbye!")
        print("\033[1m\033[34mGoodbye!\033[00m")
        engine.runAndWait()
    elif(close == 2):
        engine.say("Untill We Meet Again")
        print("\033[1m\033[34mUntill We Meet Again\033[00m")
        engine.runAndWait()
    elif(close == 3):
        engine.say("Have A Good Day")
        print("\033[1m\033[34mHave A Good Day\033[00m")
        engine.runAndWait()

def lang():
    language = input("\033[1m\033[92mEnter Your Preferred Language: \033[00m").lower()
    if language in ["english", "en"]:
        return "en"
    elif language in ["german", "de"]:
        return "de"
    elif language in ["spanish", "es"]:
        return "es"
    elif language in ["french", "fr"]:
        return "fr"
    elif language in ["galician", "gl"]:
        return "gl"
    elif language in ["basque", "eu"]:
        return "eu"
    elif language in ["italian", "it"]:
        return "it"
    elif language in ["hungarian", "hu"]:
        return "hu"
    elif language in ["lithuanian", "lt"]:
        return "lt"
    elif language in ["polish", "pl"]:
        return "pl"
    elif language in ["czech", "cs"]:
        return "cs"
    elif language in ["russian", "ru"]:
        return "ru"
    elif language in ["swedish", "se"]:
        return "se"
    else:
        print("\033[1m\033[91mLanguage not recognized.\033[00m")
        return None 

def operation(lang1):
    while True:
        ask_again()
        print_menu()
        op = input("\033[1m\033[92mEnter Operation's Number: \033[00m")
        if op == '1':
            jokes(lang1)
        elif op == '2':
            new_lang = lang()
            if new_lang:
                lang1 = new_lang 
                jokes(lang1)
        elif op == '3':
            end()
            break
        else:
            print("\033[1m\033[91mEnter A Valid Number.\033[00m")

engine.stop()