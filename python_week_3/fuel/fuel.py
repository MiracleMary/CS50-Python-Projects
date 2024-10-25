def fuel_percent(fraction):
    try:
        x, y = map(int, fraction.split("/"))
        if x < 0 or y <= 0 or x > y:
            raise ValueError
        percentage = (x / y) * 100
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return round(percentage)
    except (ValueError, ZeroDivisionError):
        return None


def main():
    while True:
        fraction = input("Fraction: ")
        percentage = fuel_percent(fraction)
        if percentage is not None:
            if percentage == "E":
                print("E")
            elif percentage == "F":
                print("F")
            else:
                print(percentage,"%", sep = "" )
            break
        else:
            print("Enter again")




if __name__ == "__main__":
    main()
