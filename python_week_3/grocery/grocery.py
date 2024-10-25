
grocery = {}

try:
    while True:
        item = input().strip().title()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
except EOFError:
    pass

sort = sorted(grocery.items(), key = lambda x: x[0])

for item, count in sort:
    print(f"{count} {item.upper()}")
