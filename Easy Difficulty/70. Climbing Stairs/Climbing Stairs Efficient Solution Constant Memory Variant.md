# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Please refer to:\
https://leetcode.com/problems/climbing-stairs/solutions/5034719/climbing-stairs-efficient-solution
# Approach
<!-- Describe your approach to solving the problem. -->
Please refer to:\
https://leetcode.com/problems/climbing-stairs/solutions/5034719/climbing-stairs-efficient-solution

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(1)$. Improvement achieved by allocating the space only for $2$ necessary storages.

# Code
```
class Solution:
    def climbStairs(self, n: int) -> int:
        step2, step1 = 1, 1
        for i in range(2, n+1):
            step2, step1 = step1, (step1 + step2)
        return step1
```