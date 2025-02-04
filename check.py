def build_triangle(triangle):
    

    dp = [[-1 for j in range(len(triangle[i]))] for i in range(len(triangle))]
    return dp
    
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

print(build_triangle(triangle))