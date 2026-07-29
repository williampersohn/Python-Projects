def main():
    inputt = input("What time is it? ")
    new = convert(inputt)
    if new >= 7 and new <= 8:
        print("breakfast time")
    if new >= 12 and new <= 13:
        print("lunch time")
    if new >= 18 and new <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)
    minutes = minutes / 60
    hours = float(hours)
    result = hours + minutes
    return result

if __name__ == "__main__":
    main()
