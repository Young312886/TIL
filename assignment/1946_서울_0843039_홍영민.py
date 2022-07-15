import textwrap
T = int(input())

for i in range(1,T+1):
    k = int(input())
    result = ''
    for j in range(1,k+1):
        alpha, numbers = input().split()
        result = result + alpha * int(numbers)
    result2 = textwrap.wrap(result, width = 10)
    print(f"#{i}")
    for k in range(len(result2)):
        print(result2[k])