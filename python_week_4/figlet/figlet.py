import random
from pyfiglet import Figlet
import sys


def random_font():
    figlet = Figlet()
    fonts = figlet.getFonts()
    return random.choice(fonts)

def main():
    if len(sys.argv) == 1:
        font = random_font()
    elif len(sys.argv) ==3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font = sys.argv[2]
    else:
        print("python figlet.py [-f/--font <font_name>]")
        sys.exit(1)

    figlet = Figlet(font=font)
    user = input("Input: ")
    print(figlet.renderText(user))



if __name__ == "__main__":
    main()
