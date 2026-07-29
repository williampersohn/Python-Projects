menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
new = 0
while True:
    try:
        order = input("Item: ").title()
        new = menu[order] + new
        print("Total: $", f"{new:.2f}", sep = "")
    except EOFError:
        print("")
        break
    except KeyError:
        pass
