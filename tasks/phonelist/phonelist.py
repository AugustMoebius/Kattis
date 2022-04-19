t = int(input())

prefixes = set()

def validate(numbers):
    for pn in numbers:
        for idx,_ in enumerate(pn):
            pfx = pn[0:idx]
            prefixes.add(pfx)
        if pn not in prefixes:
            prefixes.add(pn)
        else:
            return False
    return True

for _ in range(0, t):
    n = int(input())
    numbers = []
    valid = True
    for _ in range(0, n):
        number = input()
        #prefixes[number] = findPrefixes(number)
        numbers.append(number)
    numbers.sort(key=len, reverse=True)

    if validate(numbers):
        print("YES")
    else:
        print("NO")
    prefixes = set()
