def arrayCheck(nums):
    for i in range(len(nums-2)):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

print(arrayCheck([1, 1, 2, 3, 1]))