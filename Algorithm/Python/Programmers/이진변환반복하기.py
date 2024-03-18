def two(num):
    answer = ""
    while num:
        num, mod = divmod(num, 2)
        answer += str(mod)
    return answer[::-1]

def solution(s):
    answer = [0, 0]
    while s != "1":
        n = len(s)
        zero = s.count("0")
        answer[1] += zero
        c = n - zero
        s = two(c)
        answer[0] += 1
    return answer