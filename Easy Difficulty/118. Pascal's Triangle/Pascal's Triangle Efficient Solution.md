
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is necessary to notice some dependencies that can help to understand the inner mechanism of the triangle construction and solve the problem. The first one is how number of the elements increases in each new row, and the second pattern is how each new row is built based on the previous one.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Check base cases where $N$ is equal to $1$ or $2$.
2. Build the first base rows.
3. Build one new row on each iteration calculating its new elements based on previous row.
4. Return the result.


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity will be $O(N^2)$, as $N^2$ iterations are needed to build the triangle, where $N$ is the number of rows.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N^2)$, where $N$ is the number of rows, as the number of elements grows in arithmetic progression, which gives quadratic asymptotic.

# Code
```

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            prev_row = triangle[-1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j-1]+prev_row[j])
            row.append(1)
            triangle.append(row)
        return triangle

```