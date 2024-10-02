from collections import defaultdict
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        position = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal"
        }
        # rank = 4
        sorted_arr = sorted(score, reverse= True)
        dic = defaultdict(str)

        i = 1
        for val in sorted_arr:
            if i >= 4:
                dic[val] = str(i)
            else:
                dic[val] = position[i]

            i += 1

        ranked_list = []

        for val in score:
            ranked_list.append(dic[val])

        return ranked_list




