

# this the simple implementation using O(n) space and O(n) time complexity
def trap(height: list[int]) -> int:
    max_left = [0 for i in range(len(height))]
    max_right = [0 for i in range(len(height))]
    min_l_r = []
    resultant = 0
    
    current_max = 0
    for i in range(0, len(height)):
        max_left[i] = current_max
        if height[i] > current_max:
            current_max = height[i]
            
    current_max = 0
    for i in range(len(height)-1, -1, -1):
        max_right[i] = current_max
        if height[i] > current_max:
            current_max = height[i]
            
    for i in range(len(height)):
        cal = min(max_left[i], max_right[i]) - height[i]
        if cal >0:
            resultant += cal
    
    return resultant
# def compute_trapped_water(min_val, lst):
#     if min_val ==0: return 0
#     sum_ = 0
#     for ele in lst:
#         if ele > min_val:
#             pass
#         else:
#             sum_ += abs(min_val - ele)
#     return sum_

# def trap(height: list[int]) -> int:
    
#     trap_water = 0
#     left_pointer, right_pointer = 0, 1
    
#     while left_pointer < len(height) and right_pointer < len(height):
        
#         max_height_for_certain_time = float("-inf")
#         start_height = height[left_pointer]
        
#         max_index = 0
#         flag = False
#         while right_pointer < len(height):
#             if start_height <= height[right_pointer]:
#                 max_height_for_certain_time = height[right_pointer]
#                 max_index = right_pointer
#                 flag = True
#                 break
            
#             right_pointer += 1
            
#         trap_water += compute_trapped_water(min(start_height, max_height_for_certain_time), height[left_pointer: max_index+1])
#         if not flag :
#             left_pointer += 1
#         else:
#             left_pointer = right_pointer
#         right_pointer = left_pointer + 1
    
#     return trap_water
    
# lets implement the two pointer approach
def trap(height: list[int]) -> int:
    pass
        
    
if __name__ == "__main__":
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height =  [4,2,3]
    print(trap(height))
    
        