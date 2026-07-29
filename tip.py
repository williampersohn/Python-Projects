def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.removeprefix('$'))

    #todo

def percent_to_float(p):
    #todo
    multiplier = float(p.removesuffix('%'))
    multiplier2 = multiplier / 100
    return multiplier2

main()
