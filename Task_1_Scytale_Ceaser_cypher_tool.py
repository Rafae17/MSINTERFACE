from colorama import Fore, Back, Style, init
init(autoreset=True)

def print_scroll_art():
    scroll_color = Fore.YELLOW
    title_color = Fore.GREEN

    scroll_art = f"""{scroll_color}
        ________________________________________________________________________
     =(_________   _____________  ________________   ______________   ___________)=
    |                                                                           |
    |   {title_color}░██████╗░█████╗░██╗░░░██╗████████╗░█████╗░██╗░░░░░███████╗             {scroll_color} |
    |   {title_color}██╔════╝██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔══██╗██║░░░░░██╔════╝             {scroll_color} |
    |   {title_color}╚█████╗░██║░░╚═╝░╚████╔╝░░░░██║░░░███████║██║░░░░░█████╗░░             {scroll_color} |
    |   {title_color}░╚═══██╗██║░░██╗░░╚██╔╝░░░░░██║░░░██╔══██║██║░░░░░██╔══╝░░             {scroll_color} |
    |   {title_color}██████╔╝╚█████╔╝░░░██║░░░░░░██║░░░██║░░██║███████╗███████╗             {scroll_color} |
    |   {title_color}╚═════╝░░╚════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝             {scroll_color} |
    |  _________   _____________  ________________   ______________   ___________|
    =(___________________________________________________________________________)=
    """
    print(scroll_art)




def caesar_cipher(text, shift, mode):
    result =""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift * mode) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, 1)

def decrypt(text, shift):
    return caesar_cipher(text, shift, -1)
Prompt_COLOR = Fore.BLUE
Error_COLOR = Fore.RED
Result1_COLOR = Fore.GREEN
Result2_COLOR = Fore.MAGENTA

while True:
    print_scroll_art()
    operation = input(f"{Prompt_COLOR}Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit:\n {Style.RESET_ALL} ").lower()

    if operation == 'q' :
        break

    if operation not in ['e', 'd']:
        print(f"{Error_COLOR}Invalid operation. Please try again.{Style.RESET_ALL}")
        continue

    message = input(f"{Prompt_COLOR}Enter the message:  \n{Style.RESET_ALL}")
    shift = int(input(f"{Prompt_COLOR}Enter the shift value (1-25): \n {Style.RESET_ALL} "))

    if operation == 'e':
        result = encrypt(message, shift)
        print(f"{Result1_COLOR}Encrypted message: \n{result}{Style.RESET_ALL}")
    else:
        result = decrypt(message, shift)
        print(f"{Result2_COLOR}Decrypted message: \n{result}{Style.RESET_ALL}")