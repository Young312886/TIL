def dfs(stack,j):
    if len(stack) == 6:
        print(*stack)

    elif j >= len(nums) or 6 - len(stack) + j > len(nums):
        return
    else:
        for i in range(j,len(nums)):
            dfs(stack+[nums[i]],i+1)
while True:
    bank = list(map(int, input().split()))
    if bank[0] == 0:
        break
    else:
        n, nums = bank[0], bank[1:]
        dfs([],0)

    print()