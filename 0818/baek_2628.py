x , y = map(int, input().split())
row = [0,y]
comlumn = [0,x]
for _ in range(int(input())):
    way, idx = map(int,input().split())
    if way == 0:
        row.append(idx)
    else:
        comlumn.append(idx)
row.sort()
comlumn.sort()
max_size = 0
print(row, comlumn)
for i in range(len(row)-1):
    for j in range(len(comlumn)-1):
        size = (row[i+1]-row[i]) * (comlumn[j+1]-comlumn[j])
        if max_size < size:
            max_size = size
print(max_size)