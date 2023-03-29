def solution(today, terms, privacies):
    answer = []
    terms_dict = {i.split()[0]:i.split()[1] for i in terms}
    date_n = list(map(int, today.split(".")))
    # 날짜를 바꿔서 바로 가져오는 함수
    def date_change(date, m):
        year, month, date = map(int, date.split("."))
        month += int(m)
        if month >= 12:
            year += month//12
            month = month % 12
            if month == 0:
                year -= 1
                month = 12
        return year, month, date
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        m = terms_dict[term]
        date_a = list(date_change(date, m))
        # 리스트 형태의 날짜를 비교
        for i in range(3):
            # 만약 일자 까지 같은 경우, 삭제 대상이다
            if i == 2 and date_a[i] == date_n[i]:
                answer.append(idx+1)
                break
            # 그 외에는 일자를 못 넘기면 삭제 대상
            if date_a[i] < date_n[i]:
                answer.append(idx+1)
                break
            elif date_a[i] > date_n[i]:
                print("초과")
                break
        
    return answer