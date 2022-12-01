while True:
    N = int(input())
    if N == 0:
        break
    nums = [-100001]
    for i in range(N):
        key = int(input())
        nums.append(max(key, nums[i] + key))
    print(max(nums))
