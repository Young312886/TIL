shortcut = []
for _ in range(int(input())):
    words = list(map(str, input().split()))
    for idx, k in enumerate(words):
        if k[0].lower() not in shortcut:
            shortcut.append(k[0].lower())
            words[idx] = "["+k[0]+"]"+k[1:]
            break
    else:
        stop = False
        for idx1, word in enumerate(words):
            if stop == True:
                break
            for idx, j in enumerate(word):
                if j.lower() not in shortcut:
                    shortcut.append(j.lower())
                    word = word[:idx] + "["+j+"]" + word[idx+1:]
                    stop = True
                    break
            words[idx1] = word
    print(' '.join(words))

