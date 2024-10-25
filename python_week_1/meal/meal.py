def main():
    time = input("what's the time? ")
    time_format = convert(time)

    if 7.0 <= time_format <= 8.0:
        print ("breakfast time")
    elif 12.0 <= time_format <= 13.0:
        print ("lunch time")
    elif 18.0 <= time_format <= 19.0:
        print ("dinner time")
    else:
        print("")



def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + (minutes / 60)


if __name__ == "__main__":
    main()
