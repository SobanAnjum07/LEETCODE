

from collections import Counter
def topKFrequent(nums: list[int], k: int) -> list[int]:
        
    res = Counter(nums)
    res_lst = []
    for key in res:
        test_lst = []
        test_lst.append(key)
        test_lst.append(res[key])
        res_lst.append(test_lst)
    
    now = sorted(res_lst, key = lambda x:x[1], reverse=True)
    
    formed = []
    for i in range(k):
        formed.append(now[i][0])
    
    return formed
        
        
        
        
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    nums = [3,0,1,0]
    k = 1
    
    print(topKFrequent(nums, k))
    