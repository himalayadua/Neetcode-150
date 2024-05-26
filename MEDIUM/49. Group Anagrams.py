# Approach 1:
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #edge case
        
        #dict
        dict = {}

        #loop
        for item in strs:
            key = ''.join(sorted(item))
            if key in dict:
                dict[key].append(item)
            else:
                dict[key] = [item]

        return list(dict.values())


