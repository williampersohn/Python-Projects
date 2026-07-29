from pyfiglet import Figlet
figlet = Figlet()
import sys
import random

first = ["-f", "--font"]
if len(sys.argv) == 1:
     rand = random.choice(figlet.getFonts())
     figlet.setFont(font = rand)
     print(figlet.renderText(input("Input: ")))
elif sys.argv[2] not in figlet.getFonts() or sys.argv[1] not in first or len(sys.argv) != 3:
        print("Invalid usage")
        sys.exit(1)
else:
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(input("Input: ")))
