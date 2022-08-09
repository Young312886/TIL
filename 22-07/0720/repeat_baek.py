# # 2739
# a = int(input())
# for i in range(1,10):
#     print(f"{a} * {i} = {a*i}")

# # 10950

# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     print(a+b)

# # 8393
# a = int(input())
# result = 0
# for i in range(1,a+1):
#     result += i
# print(result)

# # 15552
# import sys
# t = int(sys.stdin.readline())
# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)

# #  2741

# a = int(input())
# for i in range(1,a+1):
#     print(i)
    
# # 2742
# a = int(input())
# for i in range(a,0,-1):
#     print(i)

#11021
# t = int(input())
# for i in range(1,t+1):
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a+b}")

# #11022
# t = int(input())
# for i in range(1,t+1):
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a} + {b} = {a+b}")

# # 10871
# n, x = map(int,input().split())
# a = list(map(int, input().split()))
# result = []
# for i in a:
#     if i < x:
#         result.append(i)
# for j in result:
#     print(j, end = ' ')

# # 10952

# while True:
#      a,b = map(int,input().split())
#      if a == 0 & b == 0:
#          break
#      print(a+b)

# # 10941

# while True:
#     try :
#         a, b = map(int,input().split())
#         print(a+b)
#     except:
#         break

# # 1110
# a = input()
# n = 0
# k = int(a)
# while True :
#     n += 1
#     j = k // 10 + k % 10
#     k = (k % 10)*10 + j % 10
#     if k == int(a):
#         print(n)
#         break