from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for el in nums:
            if el in elements:
                return True
            elements.add(el)
        return False
