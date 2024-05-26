#Approach 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = set()
        #flag = False

        for n in nums:
            if n in store:
                return True
            else:
                store.add(n)
        return False

#Approach 2
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)