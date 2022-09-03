def single(x):
    result = list(map(int,(list(str(x)))))
    return sum(result)

# t = int(input())

# for i in range(1,t+1):
#     a, b = map(int,input().split())
#     result = 0
#     for j in range(a,b+1):
#         result = result + single(j)
#     print(f"#{t} {result}")

# 시간 초과, 아마 for문이 한번도 들어가서는 안되는 거 같다
# 그렇다면 2가지 방법으로 속도를 향상시킬 수 있는데
# 효율적인 sum코드를 다시 작성하는 것
# 숫자열 리스트를 작성, 거디다가 sum을 해 버리는 것

# 문자열 환산 리스트는 runtime error가 뜸. Java에서도 안된다는 거 보면 막아둔듯
# for i in range(1,t+1):
#     a, b = map(int,input().split())
#     result = 0
#     j = list(range(a,b+1))
#     k = ''.join(map(str,j))
#     result = single(k)
#     print(f"#{i} {result}")

a = 0
b = 20
t = 0 
n = 1
while b > 0:
    low_upper = a // 10
    big_upper = b // 10
    low_down = a % 10
    big_down = b % 10
    if (big_upper - low_upper)<= 10:
        preserve = 45 * n + sum(range(0,low_down)) * n
        
    else : 
        preserve = 45 * n + sum(range(0,low_down)) * n
    t += preserve
    a = low_upper
    b = big_upper
print(t)
