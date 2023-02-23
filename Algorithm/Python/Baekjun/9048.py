T = int(input())
def dp (t, coins) :
    bank = [0] * (t+1)
    bank[0] = 1
    for i in range(t+1):
        for j in coins:
            if i+j < t+1:
                bank[i+j] += bank[i]
    print(bank)
    return bank[t]

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    t = int(input())
    print(dp(t, coins))