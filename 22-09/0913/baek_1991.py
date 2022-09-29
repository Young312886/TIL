n = int(input())
from collections import defaultdict
tree = defaultdict(list)
for i in range(n):
    nord = list(map(str, input().split()))
    tree[nord[0]] += nord[1:]
def pre_order(x):
    if x != '.':
        print(x, end='')
        pre_order(tree[x][0])
        pre_order(tree[x][1])
def in_order(x):
    if x != '.':
        in_order(tree[x][0])
        print(x, end='')
        in_order(tree[x][1])

def back_order(x):
    if x != '.':
        back_order(tree[x][0])
        back_order(tree[x][1])
        print(x, end='')
pre_order('A')
print()
in_order('A')
print()
back_order('A')
print()
