def solution(s):
    s = s.lower()
    pn = s.count("p")
    yn = s.count("y")
    
    return True if pn - yn == 0 else False