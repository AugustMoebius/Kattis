t = int(input())

numberMatrix = [set() for _ in range(10)]


def validate():
    for n_set in numberMatrix:
        for pn in n_set:
            for idx,_ in enumerate(pn):
                pfx = pn[0:idx]
                if pfx in numberMatrix[len(pfx) - 1]:
                    return False
    return True    


for _ in range(0, t):
    n = int(input())
    for _ in range(0, n):
        number = input()
        numberMatrix[len(number) - 1].add(number)

    if validate():
        print("YES")
    else:
        print("NO")

    numberMatrix = [set() for _ in range(10)]
