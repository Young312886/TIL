def counter(li, p):
    result = 0
    for i in li:
        if i >= p:
            result += 1
    return result

def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for h in range(len(citations)+1):
        count = counter(citations, h)
        if h <= count:
            if answer < h:
                answer = h
        else:
            break
    return answer