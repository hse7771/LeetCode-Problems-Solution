# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
For the experienced person it is almost immediately obvious to use the dynamic programming approach to solve this problem. Otherwise, it is necessary to think a little bit where to start. To solve the problem efficiently, the pattern of how each new potential jump appears should be determined.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Check if the new jump in the range of the previous jump.
2. If the new jump increases the range of the jump overall - update it.
3. Return whether the final place is in the range of jump or not. 
4. Do not forget that to achieve $n$ place it is sufficient to perform $n-1$ jumps.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of elements, as no more than $N$ iterations would be performed.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the number of elements, to store the elements.

# Code
```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i in range(len(nums)):
            if i <= max_jump:
                if max_jump < nums[i]+i:
                    max_jump = nums[i]+i
        return max_jump >= len(nums)-1
```