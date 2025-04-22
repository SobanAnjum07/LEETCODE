
def removeDuplicates(nums) -> int:
    j = 1

    prev = nums[0]
    count = 1
    prev_count = 1

    for i in range(1, len(nums)):

        if prev == nums[i] and prev_count >= 2:
            prev_count = 0
            continue

        else:
            nums[j] = nums[i]
            prev_count += 1
            j += 1
            prev = nums[i]

            count += 1
    print(nums)
    return count
    
nums = [0,0,1,1,1,1,2,3,3]
removeDuplicates(nums)
