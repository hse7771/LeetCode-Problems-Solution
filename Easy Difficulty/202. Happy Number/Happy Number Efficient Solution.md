# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Implement algorithm described in the problem.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Perform square summing.
2. Detect cycle or 1.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(logN)$, as the number of iterations would be $logN$.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(1)$, as it is finite number of squared digit sums.

# Code
```
class Solution:
    used_numbers = set()
    def isHappy(self, n: int) -> bool:
        self.used_numbers.add(n)
        if n == 1:
            self.used_numbers.clear()
            return True
        else:
            n1 = 0
            while n != 0:
                n1 += (n % 10)*(n % 10)
                n //= 10
            if n1 in self.used_numbers:
                return False
            return Solution.isHappy(Solution, n1)
```