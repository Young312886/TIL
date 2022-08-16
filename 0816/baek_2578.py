def check(x):
    n = 0
    diag1, diag2 = [], []
    for i in range(5):
        row, col = [], []
        for j in range(5):
            row += [x[i][j]]
            col += [x[j][i]]
        if sum(row) == 0:
            n += 1
        if sum(col) == 0:
            n += 1
    for i in range(5):
        diag1 += [x[i][i]]
        diag2 += [x[i][4 - i]]
    if sum(diag1) == 0:
        n += 1
    if sum(diag2) == 0:
        n += 1
    return n


bingo = [list(map(int, input().split())) for _ in range(5)]
call = []
for _ in range(5):
    call += list(map(int, input().split()))
for idx, k in enumerate(call):
    for row in bingo:
        try:
            new = row.index(k)
            row[new] = 0
        except:
            continue
    # print(bingo)
    result = check(bingo)
    # print(result)
    if result >= 3:
        print(idx + 1)
        break
