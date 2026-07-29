# str.replace() on string methods
def convert(saying):
    final = saying.replace(":(", "🙁").replace(":)", "🙂")
    print(final)

words = input()
convert(words)
