class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        res= []
        ind = 0
        cur = []

        self.helper(res, s, ind , cur)

        # print(res)
        return res


    def helper(self, res, s, ind, cur):

        if ind == len(s):
            res.append(list(cur))
            return 

        temp = ""

        for i in range(ind, len(s)):

            temp += s[i]

            if self.check_palindrome(temp):
                cur.append(temp)
                self.helper(res, s,  i+ 1, cur)
                cur.pop()


    def check_palindrome(self, s):

        return s[::-1] == s
