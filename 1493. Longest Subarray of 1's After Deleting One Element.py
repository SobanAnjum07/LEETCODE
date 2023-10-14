
def longestSubarray(nums: [int]) -> int:
    left, right = 0 , 0;
    k = 1
    flag = False
    
    if len(nums) > 1:
        
        for right in range(len(nums)) :
            
            if nums[right] == 0:
                flag = True
                k -=1
                
            if k < 0:
                
                if nums[left] == 0:
                    k += 1
                
                left += 1
                
        if flag:
            return right - left
        else:
            return len(nums) -1
    else:
        return 0


