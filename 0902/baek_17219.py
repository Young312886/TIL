n, m = map(int, input().split())
save = {}
for _ in range(n):
    p,q = map(str, input().split())
    save[p] = q
for _ in range(m):
    quest = input()
    print(save[quest])