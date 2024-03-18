def solution(user_id, banned_id):
    answer = []
    bann_dic = []
    bann_len = len(banned_id)
#   마스킹 된 아이디 조건에 맞는 아이디 리스트
    for st, banned in enumerate(banned_id):
        n = len(banned)
        bann_dic.append([])
        for user in user_id:
            if n != len(user):
                continue
            else:
                match = True
                for idx in range(n):
                    if banned[idx] == "*":
                        continue
                    elif banned[idx] != user[idx]:
                        match = False
                        break
                if match:
                    bann_dic[st].append(user)
    # print(bann_dic)
    # 매칭된 아이디 set 으로 구성
    def stacking(stack, idx):
        if idx == bann_len:
            answer.append(sorted(stack))
            return
        for ban_next in bann_dic[idx]:
            if ban_next in stack:
                continue
            else:
                stacking(stack + [ban_next], idx+1)
    stacking([],0)
    new = set([tuple(set(item)) for item in answer])
    # print(new)
    return len(new)