class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        

        n = len(ratings)
        total = [1] * n

        for i in range(1, n):

            if ratings[i] > ratings[i-1]:
                total[i] = total[i-1] + 1

        for i in range(n-2, -1, -1):

            if ratings[i] > ratings[i +1]:
                total[i] = max(total[i], total[i+1] + 1)

        return sum(total)