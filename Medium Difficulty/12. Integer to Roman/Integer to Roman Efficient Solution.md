# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Create alphabet connecting integers to roman numbers and then gradually translate each digit.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Use hash table to create number correspondence.
2. Using degree of ten translate each digit to roman equivalent.
3. Keep in mind that some digits are translated into several roman equivalents.
4. Return roman number converted to the string before it.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the number, as it is necessary to iterate through the whole string.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the number, to store it.
# Code
```
class Solution:
    def intToRoman(self, num: int) -> str:
        numbers_correspondence = {0: "", 1: "I", 4: "IV", 5: "V", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM",
                                  10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        number = list(map(int, list(str(num))))
        for i in range(len(number)):
            digit_with_decimal_place = number[i] * 10 ** (len(number) - i - 1)
            if digit_with_decimal_place in numbers_correspondence:
                number[i] = numbers_correspondence[digit_with_decimal_place]
            else:
                second_decimal_part = number[i] - number[i]%5 if number[i] >= 5 else 0
                number[i] = numbers_correspondence[second_decimal_part*10**(len(number) - i - 1)] + (number[i] % 5) * numbers_correspondence[10 ** (len(number) - i - 1)]
        return "".join(number)
```