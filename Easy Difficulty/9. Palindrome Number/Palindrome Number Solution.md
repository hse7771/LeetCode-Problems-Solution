# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Remember about Python slices.

# Approach
<!-- Describe your approach to solving the problem. -->
Use the slices achieving an efficient and easy solution.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity depends on the length of created string - therefore it is $O(N)$.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length(size) of the string received from the number.

# Code
```
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
```