back = [[0]*1001 for _ in range(1001)]
li = int(input())
limit = 0
for paper in range(1,li+1):
    y, x, y_len,x_len = map(int, input().split())
    for i in range(x,x+x_len):
        for j in range(y,y+y_len):
            back[i][j] = paper
count = [0]*(li+1)
for i in range(1,li+1):
    for k in back:
        line = k.count(i)
        count[i] += line
    print(count[i])