from itertools import combinations
n = int(input())

for _ in range(n):
    p = int(input())
    mbti = input().split()
    cases = combinations(mbti, 3)
    distance = 16
    for i in cases:
        if distance == 0:
            break
        dist = 0
        for j in range(4):
            if not(i[0][j] == i[1][j] == i[2][j]):
                dist += 2
            if dist >= distance:
                break
        if dist < distance:
            distance = dist
    print(distance)
