class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for num in nums:
            mydict[num] =1 + mydict.get(num, 0)

        arr = []
        for num, count in mydict.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])

        return res

        