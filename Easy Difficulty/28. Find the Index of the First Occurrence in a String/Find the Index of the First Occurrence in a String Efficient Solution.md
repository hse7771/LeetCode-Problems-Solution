# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Please refer to:\
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/4954469/find-the-index-of-the-first-occurrence-in-a-string

Solving this problem without use of built-in functions requires two loops iterating, comparing each element of the string to be searched in with each element of the string to be found.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Compare each element of "haystack" string with the first element of "needle" string.\
1.1 If elements are equal, continue comparing.\
1.2 If not, break out of the loop and continue iterating with the first loop.
2. If the second loop is over without breaking out, return the found index.
3. Return -1, otherwise.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N*M)$.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N+M)$.

# Code
```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            fl = False
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    fl = True
                    break
            if fl:
                continue
            return i
        return -1 
```