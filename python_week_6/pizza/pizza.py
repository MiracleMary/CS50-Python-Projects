import sys
import csv
from tabulate import tabulate

def load_menu(csv_filename):
    try:
        with open(csv_filename, newline = "") as csvfile:
            reader = csv.reader(csvfile)
            menu = list(reader)
        return menu
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def format_menu(menu):
    headers = menu[0]
    data = menu[1:]
    return tabulate(data, headers=headers, tablefmt="grid")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a csv file")

    menu = load_menu(filename)

    formatted_menu = format_menu(menu)

    print(formatted_menu)
