import sys
import csv


def process_csv(input_file, output_file):
    try:
        with open(input_file, "r", newline = "") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            data =[]

            for row in reader:
                name_parts = row[0].split(", ")
                first_name = name_parts[-1]
                last_name = name_parts[0].strip('"')
                house = row[1]
                data.append({"first": first_name, "last": last_name, "house": house})

        with open(output_file, "w", newline = "") as csvfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        print(f"Could not read {input_file}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_csv(input_file, output_file)

