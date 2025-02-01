class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def func(i, j, dp, obstacleGrid):

            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0

            elif i == 0 and j == 0: 
                return 1

            elif dp[i][j] != -1:
                return dp[i][j]

            else:
                up = func(i-1, j, dp, obstacleGrid)
                left = func(i, j -1, dp, obstacleGrid)                
                dp[i][j] =  up + left
                return dp[i][j]
            
        def count_ways(m, n):
            dp = [[-1 for j in range(n)] for i in range(m)]
            
            return func(m-1, n-1, dp, obstacleGrid)
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return count_ways(m,n)