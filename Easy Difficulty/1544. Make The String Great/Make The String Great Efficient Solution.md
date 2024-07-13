# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is possible just to follow the definition of good string - if two adjacent elements that make the string bad are found - remove them till no such elements are present in the string.

The stack data structure can be used to solve this problem, the first element of the stack will be compared with new one in the string and if they are bad - both of them should be removed, otherwise, the new element should be added to the stack. 
The similar logic can be performed in similar way but without using the stack explicitly.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Convert string to list to make dataset mutable.
2. Check 2 adjacent elements whether they are bad or not.\
2.1 Delete elements, make 1 step back (in stack the same result would be gotten automatically) and continue to the next iteration.\
2.2 Go to the next element (like adding new element to the stack).
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the string, as no more than $N$ comparisons may be performed.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$ where $N$ is the length of the string to store this string.

# Code
```
class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        s = list(s)
        while i <= len(s)-2:
            if s[i].lower() == s[i+1].lower() and s[i] != s[i+1]:
                s.pop(i)
                s.pop(i)
                i = max((i-1), 0)
                continue
            i += 1
        return "".join(s)
```