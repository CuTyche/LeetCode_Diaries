class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        
        def Canship(cap):
            ships = 1
            curcap = cap

            for w in weights:
                if curcap - w < 0:
                    ships+=1
                    curcap = cap
                curcap -= w
            return ships <= days


        l , r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = (l+r)//2
            if Canship(m):
                res= min(res, m)
                r = m-1
            else:
                l = m +1
        return res
