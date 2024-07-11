# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Explore the previous solutions for better understanding of this one.\
They can be found at:\
https://leetcode.com/problems/two-sum/solutions/4930729/two-sum-naive-but-quite-efficient-solution \
https://leetcode.com/problems/two-sum/solutions/4930686/two-sum-python3-sort-binary-search-solution \
Brief retelling: use of addends and one loop iteration to find the addend.

How can the speed of the find operation be increased?
The Hash Table Data Structure will help here.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Hash the data to increase find operation efficiency.
2. Find the addend using one loop itertation.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$ now because the find operation takes $O(1)$ time now.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity depends on the size of the data, therefore it is $O(N)$.

# Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            potential_pair = target - nums[i]
            if potential_pair in hash_table:
                pair_ind = nums.index(potential_pair)
                return [i, pair_ind]
            hash_table[nums[i]] = nums[i]
```