question = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

match question:
    case "forty two" | "forty-two" | "42":
        print("Yes")
    case _:
        print("No")
