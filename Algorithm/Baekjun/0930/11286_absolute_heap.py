# def order(li):
#     for i in range(len(li)):
#         for j in range(i+1,len(li)):
#             if abs(li[i]) < abs(li[j]):
#                 li[i], li[j] = li[j], li[i]
#             elif abs(li[i]) == abs(li[j]):
#                 if li[i] < li[j]:
#                     li[i], li[j] = li[j], li[i]
#     return li
#
# n = int(input())
# bank = []
# for _ in range(n):
#     key = int(input())
#     if key == 0:
#         if bank:
#             bank = order(bank)
#             print(bank.pop())
#         else:
#             print(0)
#     else:
#         bank.append(key)


import sys
input = sys.stdin.readline
import heapq
n = int(input())
bank = []
for _ in range(n):
    key = int(input())
    if key == 0:
        if bank:
            nothing, result = heapq.heappop(bank)
            print(result)
        else:
            print(0)
    else:
        heapq.heappush(bank, (abs(key),key))



