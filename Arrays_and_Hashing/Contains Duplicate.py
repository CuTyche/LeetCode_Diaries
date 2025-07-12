#Problem: https://leetcode.com/problems/contains-duplicate/description/
#Difficulty: Easy
#Tags: Array, Hashing, Sorting

class Solution(object):
    def containsDuplicate(self, nums):
        numset = set()
        for num in nums:
            if num in numset :
                return True
            else:
                numset.add(num)
        return False
