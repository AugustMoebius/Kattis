from sys import stdin

class Node():
    def __init__(self, x):
        self.x = x
        self.neighbors = {}



firstLine = stdin.readline().split(" ")
n = int(firstLine[0])
q = int(firstLine[1])

nodes = [None] * n


def parse_row():
    line_split = stdin.readline().split(" ")
    is_operation = line_split[0] == "="
    return (is_operation, int(line_split[1]), int(line_split[2]))

for _ in range(q):
    row = parse_row()
    x = row[1]
    y = row[2]


