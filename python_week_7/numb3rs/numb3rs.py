import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    if re.match(ipv4_pattern, ip):
        return True
    else:
        return False
    


if __name__ == "__main__":
    main()
