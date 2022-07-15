c = int(input())
b = list(map(int, input().split()))
place_num = int((c-1)/2)
b.sort()
median = b[place_num]
print(median)

