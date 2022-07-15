a = int(input())
result = 0
while a > 10:
    b = a % 10
    a = a // 10
    result = result + b
result = result + a
print(result)