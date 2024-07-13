# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Implement basic algorithms of converting from decimal to binary and vice versa.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Convert from binary to decimal.
2. Sum up.
3. Convert from decimal to binary.
4. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(logN)$ as it is necessary to store strings representations which lengths are calculated as $logN$.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(logN)$, where $N$ is the numbers, to store its string representations.

# Code
```
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def intTObinary(n):
            result = ""
            if n == 0:
                return "0"
            while n != 0:
                result += str(n % 2)
                n //= 2
            return result[::-1]
        

        def binaryTOint(n_str):
            n = 0
            for i in range(len(n_str)):
                n += int(n_str[i])*2**(len(n_str)-i-1)
            return n

        return (intTObinary(binaryTOint(a) + binaryTOint(b)))
```