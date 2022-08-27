n, K = map(int, input().split())
li = [0]*12 # 6학년, 2개의 성별
for _ in range(n):
    gender, grade = map(int,input().split())
    li[gender*6+grade-1] += 1

room = 0
for student in li:
    room += student//K
    if student%K !=0:
        room+= 1
print(room)