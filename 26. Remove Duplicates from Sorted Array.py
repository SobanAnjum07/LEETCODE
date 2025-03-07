class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        j = 1

        prev = nums[0]
        count = 1

        for i in range(1, len(nums)):

            if prev == nums[i]:
                continue

            else:
                nums[j] = nums[i]
                j += 1
                prev = nums[i]

                count += 1
        return count
        print(nums)