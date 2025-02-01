class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def func(i, j, dp):

            if i == 0 and j == 0: 
                return 1

            elif i < 0 or j < 0:
                return 0

            elif dp[i][j] != -1:
                return dp[i][j]

            else:
                up = func(i-1, j, dp)
                down = func(i, j -1, dp)                
                dp[i][j] =  up + down
                return dp[i][j]
            
        def count_ways(m, n):
            dp = [[-1 for j in range(n)] for i in range(m)]
            
            return func(m-1, n-1, dp)
        
        return count_ways(m,n)