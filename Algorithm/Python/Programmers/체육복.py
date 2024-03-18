def solution(n, lost, reserve):
    answer = n
    out = [1] * (n+1)
    lost.sort()
    for i in lost:
        # 여벌이 있으나 도난 당했을 경우
        if i in reserve:
            reserve.remove(i)
            continue
        out[i] = 0

    # 도난 당한 사람 숫자 그냥 확인
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i-1)
            out[i] = 1
        elif i + 1 in reserve:
            reserve.remove(i+1)
            out[i] = 1

    return answer - out.count(0)