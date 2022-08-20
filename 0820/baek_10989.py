k = int(input())
result = []
for _ in range(k):
    result.append(int(input()))
for i in range(k):
    for j in range(k-1,i,-1):
        if result[j] < result[i]:
            result[i],result[j] = result[j], result[i]
for ans in result:
    print(ans)