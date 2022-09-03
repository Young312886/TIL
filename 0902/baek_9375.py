from collections import defaultdict

for _ in range(int(input())):
    piece = int(input())
    clothe = defaultdict(int)
    for j in range(piece):
        nothing, shape = map(str, input().split())
        clothe[shape] += 1
    if clothe:
        result = 1
        for i in clothe.values():
            result *= (i+1)
        result -= 1
    else:
        result = 0
    print(result)