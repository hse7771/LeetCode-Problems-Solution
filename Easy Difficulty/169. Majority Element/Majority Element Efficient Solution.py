from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 0, None
        for number in nums:
            if count == 0:
                majority = number
                count += 1
            elif number == majority:
                count += 1
            else:
                count -= 1
        return majority
