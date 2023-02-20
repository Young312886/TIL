from collections import defaultdict
from collections import defaultdict
def solution(record):
    answer = []
    house = defaultdict(str)
    print(house)
    for i in record:
        user = list(map(str, i.split()))
        if user[0] == "Enter":
            house[user[1]] = user[2]
            answer.append((user[1],0))
        elif user[0] == "Leave":
            answer.append((user[1],1))
        elif user[0] == "Change":
            house[user[1]] = user[2]
    bank = []
    for user, action in answer:
        if action == 1:
            bank.append(f"{house[user]}님이 들어왔습니다.")
        else:
            bank.append(f"{house[user]}님이 나갔습니다.")
    return bank


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])