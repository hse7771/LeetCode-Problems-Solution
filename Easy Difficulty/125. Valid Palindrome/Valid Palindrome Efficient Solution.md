# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The first idea that should come to mind is to convert the string to the standard form (without spaces, register differences, etc.). Then, it is possible to use the basic algorithm of palindrome defining.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Convert the input string to the standard form.
2. Use basic algorithm palindrome defining, iterating from both ends simultaneously using two pointers move.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the size of the input string, as no more than $N/2$ iterations may be performed to define the palindrome.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the size of the input string, to store this string.

# Code
```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([letter for letter in s if letter.isalnum()]).lower()
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True


```