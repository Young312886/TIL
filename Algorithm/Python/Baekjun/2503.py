from itertools import permutations
n = int(input())
bank = list(permutations(['1','2','3','4','5','6','7','8','9'], 3))
for _ in range(n):
    new = []
    q, strike, ball = map(int, input().split())
    now = list(str(q))
    for comp in bank:
        s, b = 0,0
        for idx,j in enumerate(comp):
            if j == now[idx]:
                s += 1
            elif j in now:
                b += 1
        if s == strike and b == ball:
            new.append(comp)
    bank = new
print(len(bank))