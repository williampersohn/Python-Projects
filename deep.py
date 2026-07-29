input = input("What is the Answer to th Great Question of Life, the Universe, and Everything? ")

input = input.strip()

if input == "42":
    print("Yes")
elif input == "Forty Two":
    print("Yes")
elif input == "forty-two":
    print("Yes")
elif input == "forty two":
    print("Yes")
elif input == "FoRty TwO":
    print("Yes")
elif input == " 42 ":
    print("Yes")
else:
    print("No")
