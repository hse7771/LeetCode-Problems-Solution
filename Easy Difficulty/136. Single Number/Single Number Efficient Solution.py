from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        distinct = nums[0]
        for i in range(1, len(nums)):
            distinct ^= nums[i]
        return distinct
