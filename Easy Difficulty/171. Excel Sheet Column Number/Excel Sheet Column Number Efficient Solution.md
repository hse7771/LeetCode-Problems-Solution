# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is necessary just to implement basic algorithm of converting from one number system to another.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Convert to appropriate number system.
2. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity will be $O(logN)$, as $logN$ iterations could be performed maximum to complete the algorithm.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(logN)$ as the length of the string need to be stored is calculated exactly as $logN$.

# Code
```
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        correction = 64
        base = 26
        length = len(columnTitle)
        for i in range(length):
            n += (ord(columnTitle[i])-64)*base**(length - i - 1)
        return n
```