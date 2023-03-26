import colorama
from colorama import Fore, Style, Back

colorama.init(autoreset=True)

# Setting possible color scheme
R = Fore.RED + Style.BRIGHT + Back.BLACK 
G = Fore.GREEN + Style.BRIGHT + Back.BLACK 
C = Fore.CYAN + Style.BRIGHT + Back.BLACK 
Y = Fore.YELLOW + Style.BRIGHT + Back.BLACK 
B = Fore.BLUE + Back.BLACK + Style.BRIGHT

def phonenumwordlist():
    # get user input for area codes
    print(Y + "Create a wordlist specific to the targets area code/s. Best for WiFi.", Style.RESET_ALL)
    area_codes = input(C +  "Enter area codes separated by commas: ")
    output_file = input(C + "Output name and location:  ")
    
    # split area codes into a list
    area_codes = [code.strip() for code in area_codes.split(',')]

    # generate a list of phone numbers for each area code
    phone_numbers = []
    for code in area_codes:
        for i in range(10**7, 10**8):
            phone_numbers.append(code + str(i))

    # write phone numbers to a file
    with open(output_file, "w") as file:
        for number in phone_numbers:
            file.write(number + "\n")

    print(G + f"Wordlist written to {output_file}" + Style.RESET_ALL)


if __name__ == "__main__":
    phonenumwordlist()
