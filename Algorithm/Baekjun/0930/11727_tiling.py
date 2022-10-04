n = int(input())
p = [0] * (n+1)
p[1] = 1
if n >= 2:
    for i in range(2,n+1):
        if i % 2 == 1:
            p[i] = 2 * p[i-1] -1
        else:
            p[i] = 2 * p[i-1] + 1
print(p[n] % 10007)
