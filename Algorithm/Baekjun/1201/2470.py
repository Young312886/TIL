import sys
input = sys.stdin.readline
end = int(input()) -1
solution = sorted(list(map(int, input().split())))
start = 0
result = 1000000000
pair = []
while start < end:
    a,b = solution[start], solution[end]
    if abs(a+b) < result:
        pair = [a,b]
        result = abs(a+b)
    if a+b <= 0:
        start += 1
    else:
        end -= 1
for i in pair:
    print(i, end=' ')
print()