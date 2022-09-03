def Bruteforce(pattern, text):
    count = 0
    for i in range(len(text) - len(pattern)+2):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        else:
            count += 1
    return len(text) - count*(len(pattern)) + count


for t in range(1, int(input())+1):
    A, B = input().split()

    print(f'#{t} {Bruteforce(B, A)}')

set()