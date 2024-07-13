from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        s_ariphmetic = (1+n)*n//2
        return s_ariphmetic - s
