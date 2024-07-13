# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Please refer to:\
https://leetcode.com/problems/length-of-last-word/solutions/4960466/length-of-last-word
# Approach
<!-- Describe your approach to solving the problem. -->
1. Use one loop to iterate through the all string.
2. Store the previous length value in case of multiple spaces at the end of the string.
3. Return either the length or the previous length (length of the last word).

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$O(N)$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$O(N)$

# Code
```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        length_p = length
        for i in range(len(s)):
            if s[i] == " ":
                if length:
                    length_p = length
                length = -1
            length += 1
        return length or length_p
```