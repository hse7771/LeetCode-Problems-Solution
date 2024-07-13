# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Use the binary search algorithm to find the approximate root. 

# Approach
<!-- Describe your approach to solving the problem. -->
1. Implement binary search algorithm to find the approximate root.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(logN)$, as it is the time complexity of the binary search algorithm.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(1)$, constant space allocation is required for any parameter value.

# Code
```
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        while right - left != 1:
            root = (right + left) // 2
            if root*root <= x:
                left = root
            else:
                right = root
        return left
```