from sys import stdin

firstLine = stdin.readline().split(" ")
n = int(firstLine[0])
q = int(firstLine[1])

sets = []
setIdx = {}

def parse_row():
    line_split = stdin.readline().split(" ")
    is_operation = line_split[0] == "="
    return (is_operation, int(line_split[1]), int(line_split[2]))

def find_idxs(x, y):   
    x_idx = -1
    y_idx = -1
    if (x in setIdx):
        x_idx = setIdx[x]
    if (y in setIdx):
        y_idx = setIdx[y]

    return x_idx, y_idx

def update_sets(x, y):
    x_idx, y_idx = find_idxs(x, y)
    
    if x_idx == -1 and y_idx == -1:
        sets.append({x, y})
        setIdx[x] = len(sets) - 1
        setIdx[y] = len(sets) - 1
    elif y_idx == -1:
        sets[x_idx].add(y)
        setIdx[y] = setIdx[x] 
    elif x_idx == -1:
        sets[y_idx].add(x)
        setIdx[x] = setIdx[y]
    else:
        sets[x_idx] = sets[x_idx].union(sets[y_idx])
        for item in sets[y_idx]: 
            setIdx[item] = setIdx[x]
        #del sets[y_idx]

for _ in range(q):
    row = parse_row()
    x = row[1]
    y = row[2]
    if (row[0]): # Operation
        update_sets(x, y)
    else: # Question
        x_idx, y_idx = find_idxs(x, y) 
        if x == y or x_idx == y_idx and x_idx != -1:
            print("yes")
        else:
            print("no")