# class Solution:
def threeSum(self, nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i>0 and a== nums[i -1]:
            continue
        
        left, right =  i+1, len(nums) - 1
        
        while left < right:
            t_s = a + nums[left] + nums[right]
            if t_s > 0:
                right -=1
            elif t_s < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                
                left += 1
                while nums[left] == nums[left -1] and left < right:
                    l += 1
        
        