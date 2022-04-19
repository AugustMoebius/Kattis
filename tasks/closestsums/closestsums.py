#https://open.kattis.com/problems/closestsums


def findClosestSum(q, sums):
    bestSum = 99999999999
    bestDelta = 9999999999
    for sum in sums:
        delta = abs(sum - q)
        if delta < bestDelta:
            bestSum = sum
            bestDelta = delta
    return bestSum

def findSums(l):
    sums = set()
    for i1, item in enumerate(l):
        for i2, item2 in enumerate(l):
            if i1 != i2:
                sums.add(item + item2)
    return sums

def read():
    try:
        return input()
    except Exception:
        quit()

case_n = 1

while(True):
    n = int(read())
    l = []
    for _ in range(0, n):
        l.append(int(read()))
    m = int(read())
    print("Case %d:" % (case_n))
    sums = findSums(l)
    for _ in range(0, m):
        query = int(read())
        closest = findClosestSum(query, sums)
        print("Closest sum to %d is %d." % (query, closest))
    case_n += 1


