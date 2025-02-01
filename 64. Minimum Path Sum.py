class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def func(i, j, grid, dp):
            
            if i == 0 and j == 0:
                return grid[i][j]
            
            elif i < 0 or j < 0:
                return int(1e9)

            elif dp[i][j] != -1:
                return dp[i][j]

            else:

                up = grid[i][j] + func(i-1, j, grid, dp)
                left = grid[i][j] + func(i, j-1, grid, dp)

                dp[i][j] = min(up, left)

                return dp[i][j]

        def min_sum(grid):
            n = len(grid[0])
            m = len(grid)

            dp = [[-1 for j in range(n)] for i in range(m)]

            return func(m-1, n-1, grid, dp)
        
        return min_sum(grid)