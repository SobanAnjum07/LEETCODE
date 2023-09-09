# problem number 643

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