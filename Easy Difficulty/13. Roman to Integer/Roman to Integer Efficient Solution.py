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
