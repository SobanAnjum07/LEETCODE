def func(i, target, nums):

    if target == 0 : 
        return True

    if i == 0: 
        return nums[i] == target

    not_taken = func(i - 1, target, nums)

    taken = False

    if nums[i] <= target :
        taken = func(i-1, target-nums[i], nums)

    return taken | not_taken

def main():
    nums = [1,2,5]
    
    sum_ = sum(nums)
    
    if sum_ % 2 == 1: 
        return False

    return func(len(nums)-1, sum_//2, nums)

print(main())