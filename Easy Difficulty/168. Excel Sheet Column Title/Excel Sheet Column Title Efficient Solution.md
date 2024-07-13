# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To solve the problem it is necessary to apply basic idea of number systems.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Convert the number from one number system to another.
2. Mind the corner case of 0 remainder.
3. Return the result.

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
    def convertToTitle(self, columnNumber: int) -> str:
        column_title = ""
        correction = 64
        base = 26
        while columnNumber != 0:
            if columnNumber % base == 0:
                column_title += chr(base + correction)
                columnNumber //= base
                columnNumber -= 1
            else:
                column_title += chr(columnNumber % base + correction)
                columnNumber //= base
        return column_title[::-1]
```