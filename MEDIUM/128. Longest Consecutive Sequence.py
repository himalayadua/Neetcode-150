# Approach 1
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_length = 1
                
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_length += 1
                
                max_length = max(max_length, cur_length)
        
        return max_length

# Approach 2
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        ans = 0

        def dp(i):
            if i not in nset:
                return 0
            return 1 + dp(i+1)
        for n in nums:
            ans = max(ans, dp(n))
        return ans
