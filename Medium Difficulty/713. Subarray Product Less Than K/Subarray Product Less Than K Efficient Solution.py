from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        combinations = 0
        begin = 0
        current = 1
        for i in range(len(nums)):
            current *= nums[i]
            while current >= k and begin <= i:
                current //= nums[begin]
                begin += 1
            combinations += (i - begin + 1)
        return combinations
