def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if two_letters(s) and length(s) and positioning(s) and alpha(s):
        return True
    else:
        return False

def two_letters(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def positioning(s):
    digitstart = False
    for _ in s:
        if _.isdigit():
            if digitstart == False and _ == "0":
                return False
            digitstart = True
        else:
            if digitstart:
                return False
    return True


def alpha(s):
    if s.isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    main()
