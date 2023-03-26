# Package Imports
from colorama import Fore, Back, Style, init

# Module Imports
from phonepasswords import phonenumwordlist
from modifywordlist import modifywordlist
from scrapwords import scrapwords
from removedups import remove_duplicates
from leet_transform import leet_transform_wordlist
from crunch import crunch

init(autoreset=True)

# Setting possible color scheme
R = Fore.RED + Style.BRIGHT + Back.BLACK
G = Fore.GREEN + Style.BRIGHT + Back.BLACK
C = Fore.CYAN + Style.BRIGHT + Back.BLACK
Y = Fore.YELLOW + Style.BRIGHT + Back.BLACK
B = Fore.BLUE + Back.BLACK + Style.BRIGHT

banner = """
 __    __              _ __    __ _                  _ 
/ / /\ \ \___  _ __ __| / / /\ \ (_)______ _ _ __ __| |
\ \/  \/ / _ \| '__/ _` \ \/  \/ / |_  / _` | '__/ _` |
 \  /\  / (_) | | | (_| |\  /\  /| |/ / (_| | | | (_| |
  \/  \/ \___/|_|  \__,_| \/  \/ |_/___\__,_|_|  \__,_|
                                                       
"""

art = '''
──────────────────────────────────
───────▄██████████████████▄───────
────▄███████████████████████▄─────
───███████████████████████████────
──█████████████████████████████───
─████████████▀─────────▀████████──
██████████▀───────────────▀██████─
███████▀────────────────────█████▌
██████───▄▀▀▀▀▄──────▄▀▀▀▀▄──█████
█████▀──────────────────▄▄▄───████
████────▄█████▄───────▄█▀▀▀█▄──██▀
████──▄█▀────▀██─────█▀────────█▀─
─▀██───────────▀────────▄███▄──██─
──██───▄▄██▀█▄──▀▄▄▄▀─▄██▄▀────███
▄███────▀▀▀▀▀──────────────▄▄──██▐
█▄▀█──▀▀▀▄▄▄▀▀───────▀▀▄▄▄▀────█▌▐
█▐─█────────────▄───▄──────────█▌▐
█▐─▀───────▐──▄▀─────▀▄──▌─────██▐
█─▀────────▌──▀▄─────▄▀──▐─────██▀
▀█─█──────▐─────▀▀▄▀▀─────▌────█──
─▀█▀───────▄────────────▄──────█──
───█─────▄▀──▄█████████▄─▀▄───▄█──
───█────█──▄██▀░░░░░░░▀██▄─█──█───
───█▄───▀▄──▀██▄█████▄██▀─▄▀─▄█───
────█▄────▀───▀▀▀▀──▀▀▀──▀──▄█────
─────█▄────────▄▀▀▀▀▀▄─────▄█─────
──────███▄──────────────▄▄██──────
─────▄█─▀█████▄▄────▄▄████▀█▄─────
────▄█───────▀▀██████▀▀─────█▄────
───▄█─────▄▀───────────▀▄────█▄───
──▄█─────▀───────────────▀────█▄──
──────────────────────────────────
▐▌▐█▄█▌▐▀▀█▐▀▀▌─█▀─█▀─▐▌▐▀█▐▀█─█─█
▐▌▐─▀─▌▐▀▀▀▐──▌─▀█─▀█─▐▌▐▀▄▐▀▄─█─█
▐▌▐───▌▐───▐▄▄▌─▄█─▄█─▐▌▐▄█▐─█─█▄█

'''


def passwordrecon():
    print(Y + art)
    print(Y + banner)
    print(R + x)
    print(B + """Tools available
          
            1.Scrape Websites for words
            2.Create Local Phone Number Password Lists
            3.Remove Duplicate words on wordlist
            4.Crunch a Wordlist Together
            5.Common Wordlist Modifications1!
            6.Leet Transformations
            
            type exit to quit
            
            """)
    inp = input(Y + "Info>> ")
    if inp == "1":
        scrapwords()
    elif inp == "2":
        phonenumwordlist()
    elif inp == "3":
        remove_duplicates()
    elif inp == "4":
        crunch()
    elif inp == "5":
        modifywordlist()
    elif inp == "6":
        leet_transform_wordlist()
    elif inp == "exit":
        exit()
    elif inp == "help":
        print(B + """Tools available

            1.Scrape Websites for words
            2.Create Local Phone Number Password Lists
            3.Remove Duplicate words on wordlist
            4.Crunch a Wordlist Together
            5.Common Wordlist Modifications1!
            6.Leet Transformations
            
            type exit to quit
            """)
    else:
        print(R + "Please Enter a valid option")


if __name__ == "__main__":
    passwordrecon()
