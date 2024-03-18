#   초기값 세팅
answer = ''
leftx, lefty = 3, 0
rightx, righty = 3, 2

def solution(numbers, hand):
    global answer, leftx, lefty, rightx, righty
#   x, y 좌표 값은 numbers // 3, numbers % 3 값이다 + 0 은 3,1
#   x,y 좌표 값을 통해 다음 자판간의 거리 비교하여 2,5,8,0 누르기
    # 좌표값 부여
    def position(cursor, num):
        global answer, leftx, lefty, rightx, righty
        answer += cursor
        num -= 1
        if cursor == 'L':
            leftx, lefty = divmod(num, 3)
        else:
            rightx, righty = divmod(num, 3)
    
    for number in numbers:
        if number == 0:
            number = 11
        if number in [1,4,7]:
            position('L', number)

        elif number in [3,6,9]:
            position('R', number)

        else:
            # 거리 비교
            x, y = divmod(number - 1, 3)
            movement = (abs(x - leftx) + abs(y - lefty))  - (abs(x - rightx) + abs(y - righty))
            if movement < 0:
                position('L', number)
            elif movement > 0:
                position('R', number)
            else :
                if hand == 'left':
                    position('L', number)
                else :
                    position('R', number)
    return answer