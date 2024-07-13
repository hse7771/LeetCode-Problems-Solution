# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is necessary to implement pow algorithm and then extend it to make it work with inverse numbers, also not to forget about possible fast pow implementation.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Implement basic fast pow algorithm using math fact of even powers.
2. Extend it to work with inverse numbers.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(logN)$, as basic algorithm of fast pow is used, which is based on $a^n = (a*a)^\frac{n}{2}$ fact, where $N$ is even.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(logN)$, as no more than $logN$ calls are sufficient to perform to solve the problem, therefore, no more than $logN$ variables need to be allocated during the recursion calls.

# Code
```
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n *= -1
            x = 1/x
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        return x * self.myPow(x, n - 1)
```