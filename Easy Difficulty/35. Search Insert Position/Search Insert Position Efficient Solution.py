from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while right - left != 1:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle
        return right
