n, m = map(int, input().split())

def pactorial(j):
    house = [1] * (j+1)
    if j > 1:
        for i in range(2,j+1):
            house[i] = house[i-1] * i
    return house[j]
print(pactorial(n)//pactorial(m)//pactorial(n-m))
