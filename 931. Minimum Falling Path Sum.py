class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        

        def util_falling_path_sum(i,j,n,dp,matrix):
            if j < 0 or j >= n:
                return int(1e9)

            if i == 0:
                return matrix[0][j]

            elif dp[i][j] != -101:
                return dp[i][j]

            else:
                cur = matrix[i][j]
                left = cur + util_falling_path_sum(i-1,j-1,n,dp,matrix)
                up = cur + util_falling_path_sum(i-1,j,n,dp,matrix)
                right = cur + util_falling_path_sum(i-1,j+1,n,dp,matrix)

                dp[i][j] = min (left, up, right)
                return dp[i][j]

        def call_util(matrix):
            n = len(matrix)
            dp = [[-101 for j in range(n)] for i in range(n)]
            mini = int(1e9)
            for j in range(n):
                ans = util_falling_path_sum(n-1,j,n,dp,matrix)
                mini = min(ans, mini)

            # print(dp)
            return mini 

        return call_util(matrix)