# # 1244
# def switching(x):
#     if switch_condition[x-1] == 0:
#         switch_condition[x-1] = 1
#     else :
#         switch_condition[x-1] = 0

# switch_num = int(input())
# switch_condition = list(map(int, input().split()))
# student_num = int(input())
# for i in range(student_num):
#     sex, move = map(int,input().split())
#     if sex == 1:
#         for i in range(move,switch_num,move):
#             switching(i)
#     else :
#         switching(move)
#         for i in range(1,switch_num):
#             p, k = switch_condition[move-i-1], switch_condition[move+i-1]
#             if p == k:
#                 switching(move-i)
#                 switching(move+i)
#                 if (move-i-1)<= 0 or (move+i-1)>= switch_num :
#                     break
#             else :
#                 break
# for i in range(1, N+1):
#     print(switch_condition[i], end = " ")
#     if i % 20 == 0 :
#         print()


def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()