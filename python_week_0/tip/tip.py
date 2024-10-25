def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


  # TODO
def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)


# TODO
def percent_to_float(p):
    p=p.rstrip("%")
    return float(p) / 100.0


main()
