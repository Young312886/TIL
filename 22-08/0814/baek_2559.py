n, k = map(int, input().split())
temp = list(map(int,input().split()))
sum_num, max_num = sum(temp[:k]), sum(temp[:k])

for i in range(n-k):
    sum_num = sum_num - temp[i] + temp[i+k]
    max_num = max(sum_num, max_num)
print(max_num)