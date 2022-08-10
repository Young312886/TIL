
a = int(input())
for i in range(a):
    n = int(input())
    binary_list = list(map(int, input()))
    max_num = 0
    for j in range(n):
        count = 0
        if binary_list[j] == 0:
            continue
        else:
            count += 1
            while j < n-1:
                j += 1
                if binary_list[j] == 1:
                    count += 1
                    continue
                else:
                    break
        if max_num < count:
            max_num = count
    print(f'#{i + 1} {max_num}')


# 계산형 풀이

a = int(input())
for i in range(a):
    n = int(input())
    binary_list = list(map(int, input()))
    for j in range(1,n):
        binary_list[j] = binary_list[j-1]*binary_list[j] + binary_list[j]
    max_num = 0
    for k in binary_list:
        if k > max_num:
            max_num = k
    print(f'#{i + 1} {max_num}')
