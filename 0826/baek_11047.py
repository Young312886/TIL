m, k = map(int, input().split())

money = [int(input()) for _ in range(m)]
count = 0
for i in range(m-1,-1,-1):
    count += k // money[i]
    k = k % money[i]
print(count)