# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Implement proposed algorithm in task description iteratively.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Sum up all digits.
2. Repeat step 1 if not single digit.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(1)$ on defined boundaries, as the number of digits decreases extremely fast after each iterarion.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(1)$, as the necessary memory space does not depend on input data.

# Code
```
class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        while num >= 10:
            while num != 0:
                s += num % 10
                num //= 10
            num, s = s, num
        return num
```