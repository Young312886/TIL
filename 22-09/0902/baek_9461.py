for _ in range(int(input())):
    n = int(input())
    result = [0,1,1,1,2,2]
    if n <= 5:
        print(result[n])
    else:
        for k in range(6,n+1):
            result.append(result[k-1]+result[k-5])
        print(result[n])