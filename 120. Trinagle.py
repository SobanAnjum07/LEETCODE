class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def func(i, j, n, dp, trainge):

            if dp[i][j] != -1:
                return dp[i][j]
            
            elif i == n-1:
                return triangle[i][j]
            
            else:
                one = triangle[i][j] + func(i + 1, j, n, dp, triangle)
                two = triangle[i][j] + func(i + 1, j + 1, n, dp, triangle)

                dp[i][j] = min(one, two)

                return dp[i][j]

        def run_triangle(triangle):
            n = len(triangle)
            dp = [[-1 for j in range(n)] for i in range(n)]

            return func(0, 0, len(triangle), dp, triangle)


        return run_triangle(triangle)
        


