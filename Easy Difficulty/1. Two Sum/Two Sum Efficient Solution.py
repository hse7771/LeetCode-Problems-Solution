from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            potential_pair = target - nums[i]
            if potential_pair in hash_table:
                pair_ind = nums.index(potential_pair)
                return [i, pair_ind]
            hash_table[nums[i]] = nums[i]