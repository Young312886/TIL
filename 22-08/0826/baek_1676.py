n = int(input())
result = 1
while n > 0:
    result *= n
    n -= 1
for i in range(1,len(str(result))):
    if str(result)[-i] != "0":
        print(i-1)
        break
else:
    print(0)