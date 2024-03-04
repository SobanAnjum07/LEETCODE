

"""
.########..#######..##.......
.##....##.##.....##.##....##.
.....##..........##.##....##.
....##.....#######..##....##.
...##.....##........#########
...##.....##..............##.
...##.....#########.......##.
"""

def pivotIndex(nums: list) -> int:
    
    # getting the total sum
    total = sum(nums)
    # left index and sum will be zero as given from the question
    left_sum = 0
    
    for index, ele in enumerate(nums):
        
        right_sum = total - left_sum  - ele

        if right_sum == left_sum:
            return index

        left_sum += ele
        
    return -1