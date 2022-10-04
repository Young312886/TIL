n = int(input())
p = [0] * (n+1)
p[1] = 1
if n >= 2:
    p[2] = 2
    for i in range(3,n+1):
        p[i] = p[i-1] + p[i-2]
print(p[n] % 10007)
