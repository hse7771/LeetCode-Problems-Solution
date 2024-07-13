# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To avoid the slices and the strings completely integer arithmetic and reminders should be used.
# Approach
<!-- Describe your approach to solving the problem. -->
1. All negative numbers are not palindromes.
2. Calculate the length of the number using the comparison with degree of ten.
3. Using the length of the number calculate the number beginnings and endings comparing them before the first inequity.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
There will be $N/2$ comparisons, therefore the time complexity is $O(N)$. The number length calculation will not influence on the overall complexity. 

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity will be $O(1)$ as it does not depend on $N$ - length of the number.

# Code
```
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        length = 1
        while x // 10**length != 0:
            length += 1
        i = 0
        while i < length//2:
            if (x // 10**(length-1-i))%10 != x // 10** i % 10:
                return False
            i += 1
        return True
```