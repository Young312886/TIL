nums = [3,3,6,8,9]
target = 9
def tow(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            print(i, num, nums_map[target-num])
            print(nums_map)
            return [i,nums_map[target-num]]

tow(nums, target)
    