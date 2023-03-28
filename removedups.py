from colorama import Fore, Back, Style, init

init(autoreset=True)

# Setting possible color scheme
R = Fore.RED + Style.BRIGHT + Back.BLACK
G = Fore.GREEN + Style.BRIGHT + Back.BLACK
C = Fore.CYAN + Style.BRIGHT + Back.BLACK
Y = Fore.YELLOW + Style.BRIGHT + Back.BLACK
B = Fore.BLUE + Back.BLACK + Style.BRIGHT


def remove_duplicates():
    print(Y + "Remove duplicates from scraped words.")
    print(Y + "No output file, saves changes to input file.")    
    input_file = input(C + "Enter the input file name: ")

    # Read in words from input file
    with open(input_file, 'r') as f:
        words = f.read().splitlines()

    # Remove duplicates and track removed words
    unique_words = []
    removed_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
        else:
            removed_words.append(word)

    # Write unique words back to the input file
    with open(input_file, 'w') as f:
        f.write('\n'.join(unique_words))
        print(Y + f"File updated: {input_file}")

    for word in removed_words:
        print(B + f"Removed duplicate: {R}{word}{Y}")
    print(G + f'Removed {len(removed_words)} duplicate/s.')


if __name__ == '__main__':
    remove_duplicates()
