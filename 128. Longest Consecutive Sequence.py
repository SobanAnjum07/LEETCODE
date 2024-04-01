class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_num = set(nums)
        max_ = 0
        
        for n in nums:
            
            if (n-1) not in set_num:
                l = 0
                while (n+l) in set_num:
                    l += 1
            
                max_ = max(l, max_)
            
        return max_