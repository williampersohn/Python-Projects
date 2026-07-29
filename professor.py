import random

def main():
    n = get_level()
    count = 0
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 0
        while tries < 3:
            try:
                print(x, "+", y, "= ", end="")
                answer = int(input(""))
                correct = int(x) + int(y)
                if answer != correct:
                    print("EEE")
                    tries += 1
                    if tries == 3:
                        print(x, "+", y, "=", correct)
                elif answer == correct:
                    count += 1
                    break
            except ValueError:
                print("EEE")
                tries += 1
    print("Score:", count)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            list123 = [1, 2, 3]
            if n in list123:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
    return x

if __name__ == "__main__":
    main()
