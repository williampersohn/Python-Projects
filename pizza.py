import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
else:
    try:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1], "r") as file:
                tablet = []
                reader = csv.reader(file)
                for row in reader:
                    tablet.append(row)
                table = tablet[1:]
                print(tabulate(table, headers=tablet[0], tablefmt="grid"))

        else:
            print("Not a CSV file")
            sys.exit(1)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
