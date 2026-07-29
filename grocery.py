items = {}
while True:
    try:
        item = input("")
        item = item.upper()
        items[item] = items.get(item, 0) + 1
    except EOFError:
        print("")
        break
    except KeyError:
        pass
sort = sorted(items)
for item in sort:
    print(items[item], item)
