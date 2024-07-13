# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To determine whether the bit is equal 1 or 0, it is sufficient to check the remainder of the number modulo 2. 

# Approach
<!-- Describe your approach to solving the problem. -->
If the number is even, the last bit is 1, if it is odd, the last bit is 1.
It is possible to count the number of "set" bits checking every time whether the number is even or not and then dividing it by 2 (bit manipulation).

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(logN)$, as no more than $logN$ iterations will be performed to complete the algorithm.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity will be $O(1)$, as constant amount of memory is needed.

# Code
```
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += n % 2
            n //= 2
        return count

```