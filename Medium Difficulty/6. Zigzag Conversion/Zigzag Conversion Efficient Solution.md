# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is necessary to find the pattern of calculating each new index in the base string for the next character in the result one.
It can be useful to start with a doubled number of rows minus 2, as it is the first and last columns that are counted twice.
Then, to look at how indexes are changed in each separate row and find the dependence in step changes.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Check the base case, where number of rows is 1.
2. Built the string calculating the appropriate index according to the found pattern.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, as no more than $N$ iterations are necessary to solve the problem, where $N$ is the length of the input string.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the input string, to store the result one, that has the same length.

# Code
```
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        if numRows == 1:
            return s
        begin = 0
        step = numRows * 2 - 2
        while begin < numRows:
            i = 0
            index = begin
            while index < len(s):
                result += s[index]
                if begin == 0 or begin == numRows-1:
                    index += step
                else:
                    if i % 2 == 0:
                        index += step
                    else:
                        index += (numRows * 2 - 2 - step)
                i += 1
            begin += 1
            step -= 2
            if step == 0:
                step = numRows * 2 - 2
        return result
```