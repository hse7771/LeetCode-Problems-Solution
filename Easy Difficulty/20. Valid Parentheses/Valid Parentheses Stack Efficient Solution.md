# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To efficiently solve this problem, it is necessary to know whether the new parenthesis from the current iteraion is valid one or not. To obtain this knowledge, it should be compared with the last of opened parentheses if it is a closed one Otherwise, it should be remembered to be compared with the next closed bracket.
These points should bring to mind the idea about the stack data structure.

# Approach
<!-- Describe your approach to solving the problem. -->
There is no need for the full stack functionality for this problem, only necessary part should be used.

1. Create equivalence between open and closed parentheses.
2. Iterate through the string:\
2.1 Open brackets go to the stack.\
2.2 Closed brackets are compared with the first out stack element.
3. Stack should be checked for containing any elements after the complete loop.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity will be $O(N)$, where $N$ is the length(size) of the string, as no more than $N$ iterations can be performed.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length(size) of the string.

# Code
```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(" : ")", "[" : "]", "{" : "}"}
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if not stack or bracket != brackets[stack[-1]]:
                    return False
                stack.pop(-1)
        if stack:
            return False
        return True
```