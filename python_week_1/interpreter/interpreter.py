def expression(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

def main():
    user_input = input("X Y Z: ")
    x, y, z = user_input.split(" ")
    x = int(x)
    z = int(z)

    result = expression(x, y, z)

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()

