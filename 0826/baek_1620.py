import sys
n, m = map(int, sys.stdin.readline().split())
dogam = {}
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    dogam[i] = name
    dogam[name] = i
for _ in range(m):
    quest = sys.stdin.readline().strip()
    if not quest.isdigit():
        print(dogam[quest])
    else:
        print(dogam[int(quest)])