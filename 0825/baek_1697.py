k, t = map(int, input().split())
place = [0] * (max(k,t)+1)
if k == t:
    result = 0
elif t > k:
    place[k] = 0
    for j in range(k-1,0,-1):
        place[j] = k-j
    for i in range(k+1,t+1):
        if i % 2 == 0:
            place[i] = min(place[i-1], place[i//2])+1
        else:
            place[i] = min(place[i-1], place[(i+1)//2]+1)+1
    result = place[t]
elif t < k:
    result = k-t
print(result)

