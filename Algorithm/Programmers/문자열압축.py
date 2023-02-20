def solution(s):
    n, answer = len(s), len(s)
    for i in range(1,n//2+1):
        p = 0
        temp = ""
        while p <= n:
            count = 0
            now = s[p:p+i]
            while p+2*i <= n:
                if now == s[p+i:p+2*i] :
                    count += 1
                    p += i
                else:
                    break
            temp += str(count+1) if (count != 0) else ""
            temp += now
            p += i
        if answer > len(temp):
            answer = len(temp)
    return answer
print(solution("ababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdab"))