m,n = map(int, input().split())

M = []
N = []
for i in range(1,m+1):
    if m%i == 0:
        M.append(i)
for j in range(1,n+1):
    if n%j == 0:
        N.append(j)
factor = [i for i in N if i in M]
g_factor = max(factor)
s_factor = m * n // g_factor
print(g_factor)
print(s_factor)