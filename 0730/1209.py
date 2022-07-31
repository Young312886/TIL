# for i in range(10):
#     case_num = int(input())
#     numbers = list(map(int,input().split()))
#     highest = 0
#     # 가로 합 0 - 9 / 10 - 19
#     for i in range(10):
#         outcome = sum(numbers[10*i:10*i+10])
#         if outcome > highest:
#             highest = outcome
#     # 세로합 0 ,10,20--90
#     for i in range(10):
#         outcome = sum()
a = [1,2,3,4,5]
print(sum(a[ lambda x : x + 1]))