import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    main1, extension1 = sys.argv[1].split(".")
    main2, extension2 = sys.argv[2].split(".")
    correct = ["jpg", "jpeg", "png"]

    if extension1 not in correct:
        print("Invalid input")
    if extension2 not in correct:
        print("Invalid output")
        sys.exit(1)

    else:
        try:
            image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            image = ImageOps.fit(image, size = shirt.size)
            image.paste(shirt, shirt)
            image.save(sys.argv[2])
        except FileNotFoundError:
            print("Input does not exist")
            sys.exit(1)

if __name__ == "__main__":
    main()
