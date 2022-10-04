n, r = map(int, input().split())
p = n-r
factorial = [1] * (n+1)
for i in range(1,n+1):
    factorial[i] = factorial[i-1] * i
result = factorial[n] / factorial[r] / factorial[n-r]
print(int(result))