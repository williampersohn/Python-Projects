import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if ip.startswith("0"):
        return False
    if re.search(r"^.+\..+\..+\..+$", ip):
        numbers = ip.split(".")
        if len(numbers) > 4:
            return False
        try:
            for o in numbers:
                if "." in o:
                    return False
                o = int(o)
                if 0 <= o <= 255:
                    continue
                else:
                    return False
            return True
        except TypeError:
            return False
    else:
        return False



if __name__ == "__main__":
    main()
