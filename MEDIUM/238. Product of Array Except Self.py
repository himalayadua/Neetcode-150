#Approach 2:
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        res = [0] * n

        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        # left = [1, 1, 2, 6]


        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        # right = [24, 12, 4, 1]


        for i in range(n):
            res[i] = left[i] * right[i]

        return res