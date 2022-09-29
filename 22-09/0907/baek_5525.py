pn = int(input())
M = int(input())
check = list(input())
finder = ["I","O"]*pn + ["I"]

result, i, c  = 0, 0, 0

while i < M:
    if i+c < M and check[i+c] == finder[c]:
        c += 1
        if c == 2*pn+1:
            c = 0
            result += 1
            i += 1
    else:
        i += 1
        c = 0
print(result)
    