"""
..#######..##.........#######.
.##.....##.##....##..##.....##
.##........##....##.........##
.########..##....##...#######.
.##.....##.#########........##
.##.....##.......##..##.....##
..#######........##...#######.
"""

# problem number 643

# we will use a sliding window for this 
# the intuition is simple
# we will make the sum of frst k elements and then one by one remove the values from the
# sum we have 

class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        now = max_ = sum(nums[:k])

        for i in range(k, len(nums)):

            now += nums[i] - nums[i-k]

            if now > max_:
                max_ = now

        return max_/k