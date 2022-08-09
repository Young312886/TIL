# for i in range(10):
t = int(input())
buildings = list(map(int,input().split()))
light = 0
for idx, k in enumerate(buildings):
    if idx < 2 or idx > (t - 3):
        continue
    left2 = buildings[idx-2]
    left1 = buildings[idx-1]
    right2 = buildings[idx+2]
    right1 = buildings[idx+1]
    highest = max(left1,left2,right1,right2)

    if k > highest:
        light = light + k - highest
print(light)