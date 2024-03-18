def solution(s, n):
    answer = ''
    print(ord("a"), ord("z"))
    for one in s:
        if one == " ":
            answer += " "
            continue
        elif one.isupper():
            num = ord(one)
            num += n
            if num > 90:
                num -= (90 - 64)
        else:
            num = ord(one)
            num += n
            if num > 122:
                num -= (122 - 96)
        answer += chr(num)
        
    return answer