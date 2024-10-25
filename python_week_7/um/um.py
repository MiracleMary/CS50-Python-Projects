import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_pattern = r"\bum\b"
    um_matches = re.findall(um_pattern, s, flags=re.IGNORECASE)
    return len(um_matches)



if __name__ == "__main__":
    main()


