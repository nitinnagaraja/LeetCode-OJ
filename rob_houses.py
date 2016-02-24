def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    yes = 0
    no = 0
    temp = 0

    for n in nums:
        temp = no
        no = max(no, yes)
        yes = n + temp

    return max(yes, no)

a = map(int, raw_input().split())
print rob(a)
