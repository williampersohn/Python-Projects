import sys
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
else:
    try:
        counter = 0
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1], "r") as file:
                for line in file:
                    line = line.strip()
                    if line == "" or line.startswith("#"):
                        counter -= 1
                    counter += 1
                print(counter)
        else:
            print("Not a python file")
            sys.exit(1)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
