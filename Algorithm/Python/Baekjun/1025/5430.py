for _ in range(int(input())):
    calcul = list(input())
    n = int(input())
    nums = list(input().strip('[').strip(']').rstrip().split(','))
    if nums[0] == '':
        nums= []
    left, right = 0, n
    reverse = False
    result = False
    for change in calcul:
        if change == "R":
            if reverse:
                reverse = False
            else:
                reverse = True
        else:
            if left >= right:
                result = 'error'
                break
            else:
                if reverse:
                    right -= 1
                else:
                    left += 1
    if result == 'error':
        print('error')
    else:
        nums = nums[left:right]
        if reverse:
            nums = nums[::-1]
        print('['+','.join(nums)+']')