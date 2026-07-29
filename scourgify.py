import sys
import csv

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
else:
    try:
        old = sys.argv[1]
        new = sys.argv[2]
        rows = []
        with open(old) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                rows.append({"first": first.strip(), "last": last.strip(), "house": row["house"].strip()})


        with open(new, "w") as newfile:
            writer = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])
            writer.writerows(rows)


    except FileNotFoundError:
        print("Could not read", old)
        sys.exit(1)
