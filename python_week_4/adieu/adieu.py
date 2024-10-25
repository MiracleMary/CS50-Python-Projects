import inflect

def adieu(names):
    p = inflect.engine()

    for i, name in enumerate(names):
        farewell = "Adieu, adieu, to"
        if i == 0:
            farewell += f" {name}"
        elif i == 1:
            farewell += f" {names[0]} and {name}"
        else:
            farewell += f" {", ".join(names[:i])}, and {name}"
        print(farewell)


def main():
    names = []
    try:
        while True:
            name = input("Names: ")
            names.append(name)
    except EOFError:
        pass

    adieu(names)


if __name__ == "__main__":
    main()
