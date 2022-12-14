# 야구의 철칙, 잘치는 놈이 많이 처야 한다
# 는 개뿔이었다, 주자 쌓아서 쳐맞는게 항상 뼈아픈거였다
# single_score = []
# for i in range(1,9):
#     score = sum([p[i] for p in inning])
#     single_score.append([i,score])
# # print(single_score)
# single_score.sort(key=lambda x : x[1],reverse=True)
# batters = [p[0] for p in single_score[:3]] + [0] + [p[0] for p in single_score[3:]]
# print(batters)
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
inning = []
for _ in range(n):
    score = list(map(int, input().split()))
    inning.append(score)

def scoring(batters):
    start = 0
    score = 0
    for i in range(n):
        base1, base2, base3 = 0,0,0
        out = 0
        runner = []
        while out < 3:
            bating = inning[i][batters[start]]
            if bating == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif bating == 2:
                score += base3 + base2
                base1, base2, base3 = 0, 1, base1
            elif bating == 3:
                score += base3 + base2 + base1
                base1, base2 ,base3 = 0, 0, 1
            elif bating == 4:
                score += base3 + base2 + base1 + 1
                base1, base2, base3 = 0,0,0
            elif bating == 0:
                out += 1
            start = (start + 1) % 9
    return score

# 무작위 배터들 순서
batter = [i for i in range(1,9)]
batters = list(permutations(batter))
result = 0
for lineup in batters:
    lineup = list(lineup)
    lineup = lineup[:3] + [0] + lineup[3:]
    one = scoring(lineup)
    if one > result:
        result = one
print(result)
    
# 스코어 계산