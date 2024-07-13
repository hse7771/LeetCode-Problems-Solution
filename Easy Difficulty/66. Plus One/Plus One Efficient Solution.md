# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To add 1 to the number represented by separate digits in the list, it is sufficient just to increase last element and do not forget about potential additional decimal place.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Increase last digit in the array by 1.
2. Check if there is an additional decimap place going to the next digit and so on.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$ in the worst case, as it may be necessary to iterate through the whole array from the end to the beginning.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the number, to store it in the list.

# Code
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                return digits
        return digits
```