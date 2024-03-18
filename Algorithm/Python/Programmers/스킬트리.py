def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        before = -1
        error = False
        for i,s in enumerate(skill):
            if s not in tree:
                break
            pos = tree.index(s)
            if pos < before:
                error = True
                break
            before = pos
        for s in skill[i+1:]:
            if s in tree:
                error = True
                break
        if error == False:
            answer += 1
    return answer