import re

def main():
    print(count(input("Text: ")))

def count(s):
    nu = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(nu)

if __name__ == "__main__":
    main()
