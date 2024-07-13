# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Remember about crucial $XOR$ operation property.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Initialize the varible which will hold the answer at the end.
2. Apply $XOR$ operation to every number in the array using a loop.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the input array, as $N$ iterations are necessary to perform to solve the problem.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space comlexity is $O(1)$, as it does not change depending on different size of the input array.

# Code
```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        distinct = nums[0]
        for i in range(1, len(nums)):
            distinct ^= nums[i]
        return distinct

```