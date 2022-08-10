def find(list1):
    total = sum(list1)
    for i in range(8):
        for j in range(i+1, 9):
            compare = total - list1[i] - list1[j]
            if compare == 100:
                k, p = list1[i], list1[j]
                list1.remove(k)
                list1.remove(p)
                return list1
# 투포인트 전략 실패
# def find(list1):
#     total = sum(list1)
#     i, j = 0, 8
#     while i < j:
#         k, p = list1[i], list1[j]
#         print(k, p)
#         compare = total - k - p
#         if compare == 100:
#             list1.remove(k)
#             list1.remove(p)
#             return list1
#         elif compare > 100:
#             j -= 1
#         else:
#             i += 1

height = [int(input()) for _ in range (9)]

height.sort()
result = find(height)
for j in result:
    print(j)

