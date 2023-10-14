
"""
....##.....#####.....#####...##.......
..####....##...##...##...##..##....##.
....##...##.....##.##.....##.##....##.
....##...##.....##.##.....##.##....##.
....##...##.....##.##.....##.#########
....##....##...##...##...##........##.
..######...#####.....#####.........##.
"""

# problem # 1004

def longestOnes( nums: [int], k: int) -> int:
    # a = [1,1,1,0,0,0,1]
    # k = 2
    
    left, right = 0 , 0;
    
    for right in range(len(nums)) :
        
        if nums[right] == 0:
            k -=1
            
        if k < 0:
            
            if nums[left] == 0:
                k += 1
            
            left += 1
            
    
    return right - left + 1
        
if __name__ == '__main__':
    
    a = list(map(int, input().split(',')))
    
    k = int(input())
    
    l = longestOnes(a, k)
    print(l)