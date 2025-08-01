class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        def cus(n):
            return(count[n], -n)

        nums.sort(key=cus)
        return nums
        