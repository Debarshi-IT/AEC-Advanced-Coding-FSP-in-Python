# https://leetcode.com/problems/single-number/description/
# 136 Single Number
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result = result ^ num
        return result

print(Solution().singleNumber([11, 33, 22, 44, 33, 11, 22]))
print(Solution().singleNumber([10, 20, 40, 30, 20, 10, 60, 60, 30]))