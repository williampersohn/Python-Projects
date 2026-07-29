d = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}
while True:
    date = input("Date: ")
    try:
        if "/" in date:
            month, day, year = date.split("/")
            if month.isalpha():
                raise NameError
        elif "," not in date:
                raise NameError
        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split()
            if month.isalpha():
                month = d[month]
        month = int(month)
        day = int(day)
        year = int(year)
        if day > 31 or month > 12:
            raise NameError
    except NameError:
        pass
    except ValueError:
        pass
    else:
        print(year, f"{month:02}", f"{day:02}", sep="-")
        break
