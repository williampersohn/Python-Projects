expression = input("Expression: ")
first, second, third = expression.split()
first = int(first)
third = int(third)

if second == "+":
    result = float(first + third)
    print(result)
elif second == "-":
    result = float(first - third)
    print(result)
elif second == "*":
    result = float(first * third)
    print(result)
elif second == "/":
    result = float(first / third)
    print(result)
