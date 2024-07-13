# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Create correspondence alphabet to translate each roman number to integer and summing up it altogether as roman numbers already hold the information about the decimal place.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Create the alphabet.
2. Translate each digit by summing up in the result variable.
3. Return the received integer.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the string, as it is necessary to iterate through it.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the string, to sore it.
# Code
```
class Solution:
    def romanToInt(self, s: str) -> int:
        numbers_correspondence = {"I": 1, "IV": 4, "V": 5, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
                                  "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = list(s)
        n = 0
        i = 0
        while i < len(number):
            if i + 1 < len(number) and number[i]+number[i+1] in numbers_correspondence:
                n += numbers_correspondence[number[i]+number[i+1]]
                i += 2
            else:
                n += numbers_correspondence[number[i]]
                i += 1
        return n
```