for tc in range(int(input())):
    n, m = map(int, input().split())
    flag = [list(map(str, input())) for _ in range(n)]
    white = m - flag[0].count("W")
    red = m - flag[-1].count("R")
    compare = []
    compare.append([white, white, white])
    for i in range(1,n-1):
        line = flag[i]
        w = m - line.count("W")
        b = m - line.count("B")
        r = m - line.count("R")
        compare.append([w, b, r])
    compare.append([red, red, red])
    result = 50*50
    for i in range(1,n-1):
        for j in range(i+1,n):
            w = sum(k[0] for k in compare[:i])
            b = sum(k[1] for k in compare[i:j])
            r = sum(k[2] for k in compare[j:])
            result = min(result, (w+b+r))
    print(result)
