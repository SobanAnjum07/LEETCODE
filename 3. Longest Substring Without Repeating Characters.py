class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        max_ = 0
        lookup = set()
        for right in range(len(s)):

            while s[right] in lookup:
                lookup.discard(s[left])

                left += 1

            lookup.add(s[right])
            max_ = max(max_, right -left + 1)

        return max_
        