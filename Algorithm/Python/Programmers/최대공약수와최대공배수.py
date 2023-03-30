# 매우 비효율적인 코드
# 수학적으로 접근을 해도 되는 코드가 추가적으로 있다
# 반대로 유클리드 호재법을 사용하면 더욱 간단해짐
def solution(n, m):
    bound = max(n,m)
    base = [0] * (bound+1)
    border = len(base)
    def dividing(n):
        base = [0] * (border+1)
        p = 2
        while n != 1:
            if n % p == 0:
                base[p] += 1
                n /= p
            else:
                p += 1
        return base
    n_base = dividing(n)
    m_base = dividing(m)
    print(n_base, m_base)
    answer = [1,1]
    for i in range(border+1):
        if n_base[i] and m_base[i]:
            answer[0] *= i ** min(n_base[i], m_base[i])
        if n_base[i] or m_base[i]:
            answer[1] *= i ** max(n_base[i], m_base[i])
    return answer