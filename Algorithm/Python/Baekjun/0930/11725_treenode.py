n = int(input())
up = [0]*(n+1)
q = []
for _ in range(n-1):
    s, e = map(int, input().split())
    q.append((s,e))
    q.append((e,s))
q.sort()
while q:
    s,e = q.pop(0)
    if s == 1:
        up[e] = s
    elif up[s] and not up[e]:
        up[e] = s
    elif up[e] and not up[s]:
        up[s] = e


for i in up[2:]:
    print(i)