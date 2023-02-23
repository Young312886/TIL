n,m = map(int, input().split())
people = [0] * (n+1)
know = list(map(int,input().split()))
if know[0] != 0:
    for i in range(1,len(know)):
        people[know[i]] = 1
result = 0

for _ in range(m):
    party = list(map(int,input().split()))
    able = True
    for i in range(1,party[0]+1):
        if people[party[i]] == 1:
            able = False
            break
    if able == True:
        result += 1
    else:
        for i in range(1,party[0]+1):
            people[party[i]] = 1
print('result', result)


## fail