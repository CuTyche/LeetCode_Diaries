class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        res= 0
        l, r = 0, len(people)-1
        while l <= r:
            remains = limit - people[r]
            r-=1
            res+=1
            if l<= r and remains >= people[l]:
                l+=1
        return res