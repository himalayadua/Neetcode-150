# Approach1
class Solution(object):
    def mergeAlternately(self, word1, word2):

        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)
    

# Approach2
class Solution:
    def mergeAlternately(self, word1, word2):
        i,j = 0,0
        res = []
        while ( i < len(word1) or j < len(word2)):
            if i < len(word1):
                res.append(word1[i])
                i += 1
            if j < len(word2):
                res.append(word2[j])
                j += 1
        return "".join(res)


