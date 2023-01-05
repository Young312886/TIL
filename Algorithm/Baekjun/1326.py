n = int(input())
rocks = list(map(int, input().split()))
s, t = map(int, input().split())
s -= 1
t -= 1
stack = [(s,0)]
def bfs():
    while stack:
        now, times = stack.pop(0)
        if now > n or now < 0:
            continue
        elif now == t:
            return times
        if rocks[now] == 0:
            continue
        p = n // rocks[now]
        for i in range(1,p+2):
            stack.append((now+i*rocks[now],times+1))
            stack.append((now-i*rocks[now],times+1))

    return -1
print(bfs())