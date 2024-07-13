from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i in range(len(nums)):
            if i <= max_jump:
                if max_jump < nums[i]+i:
                    max_jump = nums[i]+i
        return max_jump >= len(nums)-1
