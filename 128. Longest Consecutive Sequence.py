
from collections import Counter

def longestConsecutive(nums: list[int]) -> int:
    
    hashmap = Counter(nums)
    
    cnt = 0
    
    test = next(iter(hashmap))
    # for key in hashmap:
    
    print(test, hashmap)
    
    for key in hashmap:
        print(key, end=" ")
    
    
    
if __name__ == "__main__":
    nums = [3,7,2,5,8,4,6,0,1,0]
    longestConsecutive(nums)
    
    
        
                