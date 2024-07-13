# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The sum of increasing sequence with the step of 1 can be calculated as sum of arithmetic progression.

# Approach
<!-- Describe your approach to solving the problem. -->
The formula is:
$\Large S=\frac{(a_1+a_n)}{2}\cdot n$

Then it is only necessary to compare it with the real sum of the sequence and the missing element can be calculated as a difference.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity will be $O(N)$ despite using arithmetic progression formula, as it is necessary to calculate the real sum of elements as well, and $N$ iterations will be needed to do it.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity will be $O(N)$ to store $N$ elements, where $N$ is the number of elements in the array.

# Code
```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        s_ariphmetic = (1+n)*n//2
        return s_ariphmetic - s
```