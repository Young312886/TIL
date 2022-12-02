import sys
input = sys.stdin.readline
end = int(input()) -1
solution = sorted(list(map(int, input().split())))
start = 0
result = 2000000000
pair = []
while start < end:
    a,b = solution[start], solution[end]
    if abs(a+b) < result:
        pair = [a,b]
        result = abs(a+b)
    if a+b == 0:
        break
    elif a+b > 0:
        end -= 1
    else:
        start += 1
for i in pair:
    print(i, end=' ')
print()