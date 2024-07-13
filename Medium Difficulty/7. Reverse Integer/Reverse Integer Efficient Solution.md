# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The number may be reversed using remainder and integer division approach, then, the number should be checked if it is in the boundaries. 
However, there is another approach of reversing - make a string from the integer and reverse it as a string.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Make a string from the number.
2. Reverse the string.
3. Check the sign.
4. Check the boundaries.
5. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$ as it is time complexity of string reverse operation.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the number, as it need to be stored as a string.

# Code
```
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1]
        if x[-1] == "-":
            x = "-" + x[:-1]
        return int(x) if -2**31 <= int(x) <= 2**31-1 else 0
```