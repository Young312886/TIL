N = int(input())
m = int(input())
key = [i for i in range(10)]
if m:
    drop = list(map(int, input().split()))
else:
    drop = []
for i in drop:
    key.remove(i)
result = abs(N-100)
def dfs(x):
    global result
    if x and len(x) >= len(str(N)) - 1:
        press = abs(N - int(x)) + len(x)
        if result > press:
            result = press
        if x[0] != 1 or x[0] != 9:
            return
    if len(x) > len(str(N)):
        return
    else:
        for i in key:
            dfs(x + str(i))
if key:
    dfs('')

print(result)