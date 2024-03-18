def solution(n):
    answer = ''
    while n:
        n, mod = divmod(n, 3)
        answer += str(mod)
    return int(answer, 3)