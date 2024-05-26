#Approach 1:
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for s in nums:
            frequency[s] = frequency.get(s, 0) + 1
        
        #new_nums = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1])}

        final = []
        for i in range(k):
            #final.append(x.keys().index("c"))
            #max(frequency.values()) -- max value

            #key with max value -- max(frequency, key=frequency.get)
            maxkey = max(frequency, key=frequency.get)
            final.append(maxkey)
            frequency.pop(maxkey)

        return final


