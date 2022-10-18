n , target = map(int, input().split())
def bfs(stack,count):
    new = []
    if stack:
        for i in stack:
            if i == target:
                print(count)
                return
            elif n > target:
                continue
            else:
                new.append(i*2)
                new.append(i*10+1)
        bfs(new, count+1)
    else:
        print(-1)
bfs([n],1)