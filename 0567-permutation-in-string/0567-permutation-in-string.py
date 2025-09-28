class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        s1count = Counter(s1)
        window = Counter(s2[:n])

        if s1count == window:
            return True
        
        for i in range(n, m):
            window[s2[i]] += 1
            window[s2[i-n]] -=1
            if window[s2[i-n]] ==0:
                del window[s2[i-n]]
            if window == s1count:
                return True
        return False
