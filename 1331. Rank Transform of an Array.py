from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        dic = defaultdict(int)

        sorted_array = sorted(arr)
        rank = 1
        if len(sorted_array) == 1:
            dic[sorted_array[0]] = rank
        else:
            for i in range(len(sorted_array) - 1):
                dic[sorted_array[i]] = rank
                if sorted_array[i] != sorted_array[i + 1]:
                    rank += 1
            if len(sorted_array) >=2:
                if sorted_array[len(sorted_array) - 1] != sorted_array[len(sorted_array) - 2]:
                    dic[sorted_array[len(arr) -1]] = rank

        ranked_arr = []

        for val in arr:
            ranked_arr.append(dic[val])
        
        # print(ranked_arr, arr, dic, sorted_array)
        return ranked_arr
        
