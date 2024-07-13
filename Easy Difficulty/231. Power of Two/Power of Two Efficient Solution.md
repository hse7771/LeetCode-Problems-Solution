# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem could be solved using iterative multiplication. It is also possible to use dividing and recursion in various combinations.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Multiply the start value by 2 before it reaches the target value or exceeds it.
2. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(logN)$, as it could be performed maximum $logN$ iterations, as each iteration increases the value by $2$.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(1)$, as constant memory allocation is needed.

# Code
```
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return x == n
```