class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        curr_end = farthest = jumps = 0

        for i in range(len(nums)-1):

            farthest = max(farthest, nums[i] + i)

            if i == curr_end:
                jumps += 1
                curr_end = farthest


        return jumps