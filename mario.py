def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each column in square
        for j in range(size):
            print("#", end="")
        print()

main()
