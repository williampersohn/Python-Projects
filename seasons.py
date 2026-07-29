import datetime
import inflect
import re
import sys

def main():
    print(minutes(input("Date of Birth: ")), "minutes")

def minutes(s):
    expression = re.search(r"^([0-9]{4})-(0[1-9]|1[0-2])-([0-3][0-9])$", s)
    if expression:
        given = datetime.date(int(expression[1]), int(expression[2]), int(expression[3]))
        now = datetime.date.today()
        difference = now - given
        minutes = difference.days * 24 * 60
        p = inflect.engine()
        words = p.number_to_words(minutes).capitalize()
        words2 = re.sub(r"\b and\b", "", words)
        return words2

    else:
        print("Invalid date")
        sys.exit(1)

if __name__ == "__main__":
    main()
