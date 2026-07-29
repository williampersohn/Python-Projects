CamelCase = input("CamelCase: ")
snakecase = ""

for word in CamelCase:
    if word.isupper():
        word = word.lower()
        snakecase += "_" + word
    else:
        snakecase += word

print(snakecase)
