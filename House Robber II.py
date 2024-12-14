class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(nums):
            n = len(nums)

            if n == 0: return 0
            if n ==1 : return nums[0]

            dp = [0] * n

            dp[n-1] = nums[n-1]
            dp[n-2] = max(nums[n-1], nums[n-2])
            

            for i in range(n-3, -1, -1):

                dp[i] = max(dp[i+2] + nums[i], dp[i+1])
            return dp[0]

        n = len(nums)
        
        # Edge cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
            
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

