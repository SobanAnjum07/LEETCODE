
'''
.########
.##......
.##......
.#######.
.......##
.##....##
..######.

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        def check_palindrome(string):

            return string[::-1] == string

        temp = ""
        for i in range(len(s)):

            for j in range(len(s), i, -1):

                # print(s[i:j])

                if check_palindrome(s[i:j]) and len(temp) < len(s[i:j]):
                    temp = s[i:j]

        return temp
