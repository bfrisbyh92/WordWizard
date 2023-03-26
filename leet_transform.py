import itertools
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Setting possible color scheme
R = Fore.RED + Style.BRIGHT + Back.BLACK 
G = Fore.GREEN + Style.BRIGHT + Back.BLACK 
C = Fore.CYAN + Style.BRIGHT + Back.BLACK 
Y = Fore.YELLOW + Style.BRIGHT + Back.BLACK 
B = Fore.BLUE + Back.BLACK + Style.BRIGHT

def leet_transform_wordlist():
    # User inputs for wordlist and output file
    wordlist_location = input(B +
        "Enter the location of the input wordlist file: ")
    output_file_location = input(B + 
        "Enter the desired location/name of the output file: ")

    # Open the wordlist file and read the words into a list
    with open(wordlist_location, 'r') as file:
        print(Y + "Opening wordlist...")
        wordlist = file.read().splitlines()

    # Define the leet transformations
    leet_transformations = {
        'a': ['4', '@'],
        'b': ['8'],
        'c': ['(', '{'],
        'e': ['3'],
        'i': ['1', '!', '|'],
        'l': ['1', '7'],
        'o': ['0'],
        's': ['$', '5'],
        't': ['7', '+']
    }

    # Apply leet transformations to each word and store the results in a new list
    leet_transformed_words = []
    for word in wordlist:
        # Add the original word to the list
        leet_transformed_words.append(word)

        # Generate all possible leet variations of the word
        for letter in word:
            if letter.lower() in leet_transformations:
                leet_options = [word[:word.index(letter)] + '' + transform + '' + word[word.index(letter)+1:] if letter.islower() else word[:word.index(
                    letter)] + '' + transform.upper() + '' + word[word.index(letter)+1:] for transform in leet_transformations[letter.lower()]]
                leet_transformed_words += leet_options
                print(G + "Making leet changes...")
                

    # Write the leet transformed wordlist to the output file
    with open(output_file_location, 'w') as file:
        file.write('\n'.join(leet_transformed_words))

    print(Y + f"Wordlist leet transformed and saved to {output_file_location}")


if __name__ == "__main__":
    leet_transform_wordlist()
