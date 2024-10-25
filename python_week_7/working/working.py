import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        time_pattern = r"(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)"

        match = re.search(time_pattern, s)

        if match:
            start_hour = int(match.group(1))
            start_minute = int(match.group(2) or 0)
            start_period = match.group(3)
            end_hour = int(match.group(4))
            end_minute = int(match.group(5) or 0)
            end_period = match.group(6)

            if start_hour < 1 or start_hour > 12 or start_minute < 0 or start_minute > 59:
                raise ValueError
            if end_hour < 1 or end_hour > 12 or end_minute < 0 or end_minute > 59:
                raise ValueError

            if start_period == "PM" and start_hour != 12:
                start_hour +=12
            elif start_period == "AM" and start_hour == 12:
                start_hour = 0

            if end_period == "PM" and end_hour != 12:
                end_hour += 12
            elif end_period == "AM" and end_hour == 12:
                end_hour = 0

            return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
        else:
            raise ValueError
    except ValueError as e:
        raise ValueError



if __name__ == "__main__":
    main()
