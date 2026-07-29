import validators

def main():
    print(valida(input("Email Address: ")))

def valida(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
