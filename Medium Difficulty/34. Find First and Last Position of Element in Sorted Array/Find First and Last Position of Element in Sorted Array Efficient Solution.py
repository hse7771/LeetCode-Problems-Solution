from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        positions = [-1, -1]
        left, right = -1, len(nums)
        if nums:
            while right - left != 1:
                middle = (left + right) // 2
                if nums[middle] >= target:
                    right = middle
                else:
                    left = middle
            if right < len(nums) and nums[right] == target:
                positions[0] = right
            left, right = right-1, len(nums)
            while right - left != 1:
                middle = (left + right) // 2
                if nums[middle] <= target:
                    left = middle
                else:
                    right = middle
            if nums[left] == target:
                positions[1] = left
        return positions
