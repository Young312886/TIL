n, m = map(int, input().split())
numbers = list(map(int, input().split()))
max = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            stack = numbers[i] + numbers[j]+ numbers[k]
            if stack > m:
                continue
            else:
                if stack > max:
                    max = stack
print(max)
