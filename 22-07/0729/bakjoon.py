# 2798

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# max_num = 0
# result = 0
# nums.sort()
# for i in range(n):
#     for j in range(i,n):
#         right = n-1
#         while right > j:
#             black = nums[i] + nums[j] + nums[right]
#             if black > m:
#                 right -= 1
#                 continue
#             else : 
#                 if black > max_num:
#                     max_num = black
#                     right -= 1
#                 else : 
#                     right -= 1

# print(max_num)

#2231
# t = int(input())
# result = 0
# for i in range(1,t+1):
#     K = list(map(int,str(i)))
#     if t == sum(K)+i:
#         result = i
#         break
#     if i == t:
#         result = 0
# print(result)

#7568

# t = int(input())
# weight = []
# height = []
# rank = [1]*t
# for i in range(t):
#     x,y = map(int,input().split())
#     weight.append(x)
#     height.append(y)
# for j in range(t):
#     for k in range(t):

#         if (weight[j] < weight[k]) and (height[j] < height[k]):
#             # print(weight[j],weight[k],height[j].height[k])
#             rank[j] = rank[j] + 1
#         else :
#             continue

# for i in rank:
#     print(i, end = ' ')

# 동시에 크다 우위 애매하다 동급 아래다 아래

# 1018
def line_change(x,key):
    change = 0
    if x[0] == key == "B":
        x[0] = "W"
        change += 1 
    elif x[0] == key == "W":
        x[0] = "B"
        change += 1
    for i in range(len(x)-1):
        if x[i] == x[i+1] == "B":
            x[i+1] = "W"
            change+=1
        elif i == x[i+1] == "W":
            x[i+1] = "B"
            change+=1
        else :
            continue
    return x, change

n, m = map(int,input().split())
board = []
for i in range(n):
    lines = list(str(input()))
    board.append(lines)
print(board)
min_num = 64
for i in range(0,n-7):
    for j in range(0,m-7):
        k = 0
        change_num = 0
        while k < 8:
            if k == 0:
                line = board[i][j:j+7]
                first_key = line[0]
                first_line,change = line_change(line,first_key)
                change_num += change
                first_key = first_line[0]
            line = board[i+k][j:j+8]
            k += 1
            first_line, change = line_change(line,first_key)
            first_key = first_line[0]
            change_num += change
        if change_num < min_num : 
            min_num = change_num
print(min_num)
        

# 8칸씩 나눠 버리기

