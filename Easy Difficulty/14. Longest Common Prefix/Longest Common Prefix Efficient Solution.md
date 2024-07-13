# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To solve the problem efficiently it is necessary to iterate through the all strings simultaneously.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Find the shortest string, as the common prefix can not be longer than the minimum unit of the list.
2. Iterate through the all strings simultaneously checking the equivalence and adding new elements to the common prefix if necessary.
3. Return received common prefix.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(M*N)$, where $M$ is the number of strings in the list and $N$ is the length of the shortest string.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of all strings in the list.

# Code
```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        mn_str = min(strs, key=len)
        for i in range(len(mn_str)):
            for el in strs:
                if mn_str[i] != el[i]:
                    return common_prefix
            common_prefix += mn_str[i]
        return common_prefix
```