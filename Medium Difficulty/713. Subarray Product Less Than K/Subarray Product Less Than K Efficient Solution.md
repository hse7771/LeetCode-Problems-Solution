# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Please refer to:\
https://leetcode.com/problems/subarray-product-less-than-k/solutions/4943324/subarray-product-less-than-k-efficient-solution
# Approach
<!-- Describe your approach to solving the problem. -->
To increase the efficiency, the redundant comparisons may be removed.
It can be noted that after certain element the current sequence product is always greater or equal k, therefore the if block from the previous solution can be removed and while loop condition should be slightly modified to make combination calculation formula work for both less than k product and greater or equal k product.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$O(N)$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$O(N)$

# Code
```
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
```