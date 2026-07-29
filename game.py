import random
n = input("Level: ")
while True:
    if not n.isdigit():
        n = input("Level: ")
    elif int(n) <= 0:
        n = int(input("Level: "))
        n = str(n)
    else:
        break
n = int(n)
right = random.randint(1, n)
def guess():
    g = input("Guess: ")
    while True:
        if not g.isdigit():
            g = input("Guess: ")
        elif int(g) <= 0:
            g = int(input("Guess: "))
            g = str(g)
        else:
            return g
a = False
while a == False:
    g = guess()
    g = int(g)
    if g == right:
        print("Just right!")
        a = True
    elif g <= right:
        print("Too small!")
        g = str(g)
        continue
    elif g >= right:
        print("Too large!")
        g = str(g)
        continue
