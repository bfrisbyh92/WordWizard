# Package Imports
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

# Setting possible color scheme
R = Fore.RED + Style.BRIGHT + Back.BLACK 
G = Fore.GREEN + Style.BRIGHT + Back.BLACK 
C = Fore.CYAN + Style.BRIGHT + Back.BLACK 
Y = Fore.YELLOW + Style.BRIGHT + Back.BLACK 
B = Fore.BLUE + Back.BLACK + Style.BRIGHT

def modifywordlist():
    # Getting the needed User Inputs so they have control
    file_path = input(B + "Enter the file path of a word list you want to alter: ")
    suffix = input(B + "Enter charachters you want appended to word: ")
    capitalize_choice = input(B + "Do you want to capitalize a specific characters in each word? (yes or no): ")
    if capitalize_choice.lower() == 'yes':
        capitalize_index = int(input(B + "Enter the index of the character to capitalize (starting from 0): "))
    else:
        capitalize_index = None
    output_file = input(B + "Enter the file path and name for the output file: ")

    # Let's open the file...
    with open(file_path, 'r') as f:
        word_list = [line.strip() for line in f]

    # Handle the business
    modified_list = []
    for word in word_list:
        modified_word = word + suffix
        if capitalize_index is not None and capitalize_index < len(modified_word):
            modified_word = modified_word[:capitalize_index] + \
                modified_word[capitalize_index:].capitalize()
        modified_list.append(modified_word)
        print(G + modified_word)

    # We need to write the file, so that we keep the condition of the original wordlist.
    with open(output_file, 'w') as f:
        print(Y + f"File written to {output_file}")
        f.write('\n'.join(modified_list))


# Ensuring that this function only runs if it's intentionally called.
if __name__ == "__main__":
    modifywordlist()
