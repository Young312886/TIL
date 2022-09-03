n = int(input())
k = list(map(int, input().split()))
k.sort()
time = 0
for i in range(n):
    time += k[i]*(n-i)
print(time)