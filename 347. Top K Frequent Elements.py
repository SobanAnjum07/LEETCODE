
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums).most_common()
        ret_list = []
        for i in range(k):
            ret_list.append(res[i][0])
        
        return ret_list
