n = int(input())
left = [0]*(n+1)
right = [0]*(n+1)

chart = list(map(int,input().split()))
for i in range(0,len(chart),2):
    print(i)
    if left[chart[i]] == 0:
        left[chart[i]] = chart[i+1]
    else:
        right[chart[i]] = chart[i+1]
def preorder(x):
    print(x)
    if left[x]:
        preorder(left[x])
    if right[x]:
        preorder(right[x])
preorder(1)

