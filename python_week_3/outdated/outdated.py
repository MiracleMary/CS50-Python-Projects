months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        month,day,year = date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            m,d,year = date.split(" ")
            for i in range(len(months)):
                if m == months[i]:
                    month = i + 1
            day = d.replace(",", "")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break

        except:
            pass

print(f"{year}-{int(month):02}-{int(day):02}")

