class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        if len(nums) %2 == 0:
            median = (nums[len(nums)//2 -1] + nums[len(nums)//2]) / 2
            return median
        
        return float(nums[len(nums) //2 ])

