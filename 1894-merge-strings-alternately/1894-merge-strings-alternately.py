class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n , m = len(word1) , len(word2)
        res=[]
        i = j = 0
        while i < n and j < m:
            if i<n:
                res.append(word1[i])
            if j < m :
                res.append(word2[j])
            i+=1
            j+=1

        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
