def main():
    I = input("Input: ")
    print("Output:", shorten(I))

def shorten(word):
    new = ""
    for c in word:
        if c.endswith(("a", "e", "i", "o", "u", "O", "A", "I", "E","U")):
            c.replace("a", "")
            c.replace("e", "")
            c.replace("i", "")
            c.replace("o", "")
            c.replace("u", "")
            c.replace("O", "")
            c.replace("A", "")
            c.replace("I", "")
            c.replace("E", "")
            c.replace("U", "")
        else:
            new += c
    return new

if __name__ == "__main__":
    main()
