def solution(new_id):
    #1 소문자
    new_id = new_id.lower()

    #2 특수문자 제거
    for symbol in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id = new_id.replace(str(symbol), '')
    
    #3 ..연속이면 .으로 치환
    while True:
        first = len(new_id)
        new_id = new_id.replace('..','.')
        if first == len(new_id):
            break
        
    #4 . 처음 끝 제거
    new_id = new_id.strip('.')
    
    #5 빈 문자열 = a        
    if not new_id:
        new_id = 'a'
        
    #6 15자 이상 탈락 및 . 삭제
    if len(new_id) >= 16:
        new_id = new_id[:15].strip('.')
    
    #7 2자 이하 길이 확장
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id