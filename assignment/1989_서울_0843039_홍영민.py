T = int(input())
for c in range(1, T + 1):
    result = 0
    cases = list(input().strip())
    another = cases.copy()
    cases.reverse()
    if (another == cases) :
        result = 1
    else : 
        result = 0
    print(f"#{c} {result}")