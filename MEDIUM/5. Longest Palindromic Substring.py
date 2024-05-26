class Solution:
    def longestPalindrome(self, s: str) -> str:
        # edge case: 1 <= s.length
        if len(s) <= 1:
            return s
        
        def expander(left, right):
            #needs to run until a particular condition
            #condition -> palindrome found
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            #comes to this step when current left and right aren't matching
            #so slicing shouldn't include chars at position left and right
            return s[left+1 : right]

        #variables to store the longest palindromic substring found
        pstring = s[0]

        #loop through all possible center indices in the string
        for i in range(len(s) - 1):
            #now there can be two cases
            #"abba"
            #"aba"
            odd = expander(i, i)
            even = expander(i, i+1)

            #compare pallindrome found with `pstring`
            if len(odd) > len(pstring):
                pstring = odd
            if len(even) > len(pstring):
                pstring = even
            
        return pstring

