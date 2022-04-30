#https://open.kattis.com/problems/joinstrings
from sys import stdin
from sys import stdout

class Node:
    child = None
    leaf = None
    def __init__(self, value):
        self.value = value
    
    def add_child(self, node):
        if (self.leaf == None):
            self.child = node
        else: 
            self.leaf.child = node
        
        if (node.leaf != None):
            self.leaf = node.leaf
        else:
            self.leaf = node
    
    def print(self):
        node = self
        while (node != None):
            stdout.write(node.value)
            node = node.child
        

n = int(stdin.readline())
m = n - 1


nodes = []

for _ in range(n):
    nodes.append(Node(stdin.readline().replace("\n", "")))

if (m == 0):
    print(nodes[0].value)
else:
    for _ in range(m):
        split = stdin.readline().split(" ")
        a = nodes[int(split[0]) - 1]
        b = nodes[int(split[1]) - 1]
        a.add_child(b)
    a.print()


    



    








