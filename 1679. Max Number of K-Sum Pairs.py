# problem number 1679

"""
 ________  _______   ________  ________  ________  ___  ________  _________  ___  ________  ________
|\   ___ \|\  ___ \ |\   ____\|\   ____\|\   __  \|\  \|\   __  \|\___   ___\\  \|\   __  \|\   ___  \
\ \  \_|\ \ \   __/|\ \  \___|\ \  \___|\ \  \|\  \ \  \ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \
 \ \  \ \\ \ \  \_|/_\ \_____  \ \  \    \ \   _  _\ \  \ \   ____\   \ \  \ \ \  \ \  \\\  \ \  \\ \  \
  \ \  \_\\ \ \  \_|\ \|____|\  \ \  \____\ \  \\  \\ \  \ \  \___|    \ \  \ \ \  \ \  \\\  \ \  \\ \  \
   \ \_______\ \_______\____\_\  \ \_______\ \__\\ _\\ \__\ \__\        \ \__\ \ \__\ \_______\ \__\\ \__\
    \|_______|\|_______|\_________\|_______|\|__|\|__|\|__|\|__|         \|__|  \|__|\|_______|\|__| \|__|
                       \|_________|


"""

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