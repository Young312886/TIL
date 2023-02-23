n = int(input())
for _ in range(n):
    si, sj = 0,0
    go = list(input())
    d = [(0,1),(1,0)]
    head, back = 0, 1
    sx, sy, bx, by = 0,0,0,0
    for i in go:
        if i == 'L':
            head = head + 1
            if head % 2 == 0:
                back *= -1
            head = head % 2
        elif i == 'R':
            head = head + 1
            if head % 2 == 1:
                back *= -1
            head = head % 2
        elif i == 'F':
            di, dj = d[head]
            si += back * di
            sj += back * dj
        elif i == 'B':
            di, dj = d[head]
            si += back *(-1) * di
            sj += back *(-1) * dj
        if si < sx:
            sx = si
        if sj < sy:
            sy = sj
        if bx < si:
            bx = si
        if by < sj:
            by = sj
    print((bx-sx) * (by-sy))