base = input()
dic = {'q':0,'u':1,'a':2,'c':3,'k':4}
ans = [0] * 500
key = set()
if len(base)%5: 
    print(-1)
    quit()
def duck():
    for i in base:
        for p in range(500):
            if ans[p] == dic[i]:
                ans[p] += 1
                if ans[p] == 5:
                    ans[p] = 0
                    if i not in key:
                        key.add(p)
                break
    print(len(key) if (len(key) and sum(ans) == 0) else -1)
duck()