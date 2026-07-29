import inflect
p = inflect.engine()
names = []
while True:
    try:
        name = input()
        names.append(name)
    except EOFError:
        break
names = p.join(names)
print("Adieu, adieu, to", names)
