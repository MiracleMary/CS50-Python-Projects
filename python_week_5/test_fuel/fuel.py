def main():
     while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            break
        except ValueError:
                print("try again")



def convert(fraction: str)->int:
        x, y = fraction.split("/")

        if not(x.isdigit() and y.isdigit()):
            raise ValueError()
        else:
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError()
            if x > y:
                raise ValueError()
        percentage = round((x / y) * 100)
        return int(percentage)


def gauge(percentage:int)-> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
