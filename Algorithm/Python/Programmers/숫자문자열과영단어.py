def solution(s):
    At = ['zero', 'one','two', 'three','four', 'five', 'six','seven','eight','nine']
    for i in range(len(At)):
        s = s.replace (At[i],str(i))
    answer = int(s)
    return answer