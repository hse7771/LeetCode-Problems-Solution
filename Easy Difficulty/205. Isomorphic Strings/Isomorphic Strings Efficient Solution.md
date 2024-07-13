# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
There is need to remember each element pair relevance solving this problem. It should bring to mind the idea of hash tables data structure or built-in dict in Python.

# Approach
<!-- Describe your approach to solving the problem. -->
As each element can have only one relevance, it is logical to store the first such relevance and check if it is unique iterating through the string.

1. Create hash table
2. Iterate through the string \
2.1 Check the element in hash table keys\
2.2 Check the element pair in hash table values\
2.3 Add pair to hash table if necessary\
2.4 Check the pair relevance
3. Return true if no breakout has been previously

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the string. Keep in mind that both strings have the same length.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the string, as it may need to store $N$ elements in the hash table.

# Code
```
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        relevance = {}
        for i in range(len(s)):
            if s[i] not in relevance:
                if t[i] in relevance.values():
                    return False
                relevance[s[i]] = t[i]
            else:
                if relevance[s[i]] != t[i]:
                    return False
        return True
```