def solution(answers):
    a1, a2, a3 = 0,0,0
    s3base = [3,3,1,1,2,2,4,4,5,5]
    s2base = [2,1,2,3,2,4,2,5]
    for idx , answer in enumerate(answers):
        s1 = idx % 5 + 1
        s2 = s2base[idx % 8 ]
        s3 = s3base[idx % 10]
        # print(s1,s2,s3)
        if answer == s1:
            a1 += 1
        if answer == s2:
            a2 += 1
        if answer == s3:
            a3 += 1
    answer = []
    score = max(a1, a2, a3)
    # print(a1, a2, a3)
    if score == a1:
        answer.append(1)
    if score == a2:
        answer.append(2)
    if score == a3:
        answer.append(3)
    return sorted(answer)