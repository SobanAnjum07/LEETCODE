from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        
        for s in strs:
            counter = [0] * 26
            
            for c in s:
                counter[ord(c) - ord("a")] += 1
                
            ret[tuple(counter)].append(s)
            
        return ret.values()