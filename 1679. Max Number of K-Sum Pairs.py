# problem number 1679


# This is for making a hashmap for the nums array
# this will return the hashmap that will contain the total count of the each value of the array
from collections import Counter;

class Solution:
    def maxOperations(self, nums, k: int) -> int:
    
        counter = Counter(nums)
        count = 0
        for num in nums:
            # This is for making the complenment hence we will check whether
            # complement of that number exists or not.
            complement = k - num
            
            if counter[complement] > 0 and counter[num] > 0:
                if num == complement and counter[num] < 2 :
                    continue
                count += 1
                counter[complement] -=1
                counter[num] -=1
            
        return count