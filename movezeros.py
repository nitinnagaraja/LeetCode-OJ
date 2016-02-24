def movezeros(nums):
    r = 0
    w = 0
        
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[r], nums[w] = nums[w], nums[r]
            r += 1
            w += 1

        else:
            r += 1

        print r, w, a

    return nums

a = map(int, raw_input().split())
print movezeros(a)
