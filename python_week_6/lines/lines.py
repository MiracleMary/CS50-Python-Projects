import sys
import os

def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            code_lines = 0
            multiline = False

            for line in lines:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if multiline:
                    if '"""' in line or "'''" in line:
                        multiline = False
                    continue
                elif line.startswith('"""') or line.startswith ("'''"):
                    multiline = True
                    continue

                code_lines += 1

            return code_lines

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        print("Not a python file")
        sys.exit(1)

    if not os.path.exists(filename):
        print("File does not exist")
        sys.exit(1)

    loc = count_lines(filename)
    print(loc)




