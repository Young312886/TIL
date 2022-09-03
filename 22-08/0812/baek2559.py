k, n = map(int, input().split())
temper = list(map(int, input().split()))
sum_num = sum(temper[:n])
max_num = sum_num
for i in range(n,k):
    sum_num = sum_num - temper[i-n] + temper[i]
    max_num = max(max_num,sum_num)
print(max_num)
