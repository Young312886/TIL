def pactorial(x):
    new = 1
    for i in range(2,x+1):
        new = new * i
        while True:
            if new % 10 == 0:
                new = new // 10
            else:
                break
    return new

target = int(input())
result = pactorial(target)
print(str(result)[-5:])
