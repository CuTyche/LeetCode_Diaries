class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0 , len(s)-1
        while l < r:
            if s[l] != s[r]:
                return (self.ispalid(s,l+1, r) or self.ispalid(s, l, r-1))
            l+=1
            r-=1
        return True

    def ispalid(self,s,l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True