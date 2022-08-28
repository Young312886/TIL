for tc in range(1,11):
    v, dots = map(int, input().split())
    chart = [[] for _ in range(v+1)]
    income = [[] for _ in range(v+1)]
    link = list(map(int, input().split()))
    stack = []
    for i in range(dots):
        x, y = link[2*i], link[2*i + 1]
        chart[x].append(y)
        income[y].append(x)
    # 시작점 설정
    for i in range(1,v+1):
        if income[i] == []:
            stack.append(i)
    print(chart, income)
    print(stack)
    # 이전에 방문해야 하는데 방문을 했는가? 는 어떻게 확인하지?
    result = []
    visited = [0]*(v+1)
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            result.append(v)
            for i in chart[v]:
                for j in income[i]:
                    if j not in result:
                        break
                else:
                    stack.append(i)
    print(f'#{tc}',*result)