# Approach 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicts = {}
        dictt = {}
        for char in s:
            dicts[char] = dicts.get(char, 0) + 1

        for char in t:
            dictt[char] = dictt.get(char, 0) + 1

        return dicts == dictt
 

# Approach 2:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1

        for char in t:
            if char not in dict:
                return False
            if dict[char] == 0:
                return False
            dict[char] -= 1
        return True
 