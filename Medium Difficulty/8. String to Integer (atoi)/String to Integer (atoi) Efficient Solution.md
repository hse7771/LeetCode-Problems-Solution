# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Check all conditions for valid convertation according to the requirements in the problem.
# Approach
<!-- Describe your approach to solving the problem. -->
Check gradually one requirement after another one.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the string because of need to iterate through the string.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the string, to store the string.

# Code
```
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = False
        if not s:
            return 0
        if s[0] in "+-":
            if s[0] == "-":
                sign = True
            s = s[1:]
        n = ""
        for digit in s:
            if digit.isdigit():
                n += digit
            else:
                break
        n = n or 0
        n = int(n)
        if sign:
            n *= -1
        if n > 2**31 - 1:
            return 2**31 - 1
        if n < -2**31:
            return -2**31
        return n
```