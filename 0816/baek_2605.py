people = int(input())
place = [0]
ticket = list(map(int,input().split()))
for i in range(people):
    place = place[:ticket[i]+1] + [i+1] + place[ticket[i]+1:]
print(*place[:0:-1])