# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Implement algorithm that checks if the number has some factor different from $2,3,5$. It can be done by dividing by all factors from the list and comparing the result with $1$. If there is at least $1$ other factor in the number, the result will not be equal to $1$.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Divide the number by all 'ugly' prime factors.
2. Check if the number is equal to $1$.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $logN$, as number is divided by 2 at least on each iteration.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(1)$, as necessary memory space is constant.

# Code
```
class Solution:
    def isUgly(self, n: int) -> bool:
        for div in [2, 3, 5]:
            while n % div == 0 and n != 0:
                n //= div
        return n == 1
```