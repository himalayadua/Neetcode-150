# Approach 1:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True

# Approach 2:
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        rev_s=s[::-1]
        
        if s==rev_s:
            return True
        else:
            return False
