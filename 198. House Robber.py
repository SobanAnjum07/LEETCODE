class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-1], nums[n-2])
        
        for i in range(n-3, -1, -1):
            
            dp[i] = max(nums[i] + dp[i + 2], dp[i+1])
            
        return dp[0]
        
        