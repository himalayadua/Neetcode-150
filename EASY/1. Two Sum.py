from typing import List

#Approach 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        #hash table to store value and index
        number_map = {}

        #store each element and index in the hash table
        for i in range(len(nums)):
            number_map[nums[i]] = i

        #check if the complement of each element exists in the hash table
        for i in range(len(nums)):
            complement = target - nums[i]

            #if it does -> that's our answer
            if complement in number_map and number_map[complement] != i:
                return [i, number_map[complement]]
            

#Approach 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums:
                ind = nums.index(complement)
                if i != ind:
                    return([i,ind])