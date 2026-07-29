def main():
        x = input("Fraction: ")
        per = convert(x)
        print(gauge(per))

def convert(fraction):
    try:
        if "-" in fraction:
            raise ValueError
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)

        if numerator > denominator:
            raise ValueError
        if denominator == 0:
            raise ZeroDivisionError

        calc = numerator / denominator
        percentage = calc * 100
        percentage = int(round(percentage))
        return percentage
    except ValueError:
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        finish = str(percentage) + "%"
        return finish

if __name__ == "__main__":
    main()
