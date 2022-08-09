t = int(input())
formation = dict()
for i in range(t):
    a,b = map(int, input().split())
    formation[a] = b
right_max = max(formation.keys())
height_max = max(formation.values())
pillar = [0]*right_max
for i,j in formation.items():
    pillar[i-1] = j
# 가장 높은 곳 찾기
center = [i for i, x in enumerate(pillar) if x == height_max]
# print(center)
for i in range(center[0], center[-1]):
    pillar[i] = height_max
## 왼쪽 끝  / 오른쪽 끝 / 가장 높은 곳
# 우선, 왼쪽 끝에서 시작, 후 가장 높은곳을 도달 / 이후 낮은곳으로 전향
# 가장 높은 곳보다 낮은가? 
    #그럼 이전보다 높은가?
    #안 높으면 이전 높이보다 높은지 확인
        # 높으면 새로 높이 주고 그 높이로 밀자
        # 안 높으면 앞의 높이로 밀거다
# 이걸 높은곳 이후로 반대로 돌리면 된다.
def switching(x,y,step = 1):
    global pillar
    high = 0
    for i in range(x,y,step):
        height = pillar[i]
        if height > high :
            high = height
        if high > height:
            pillar[i] = high
    return pillar
pillar = switching(0,center[0]+1)
pillar = switching(right_max-1, center[-1]-1,step = -1)
print(sum(pillar))
    
    

    