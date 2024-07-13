class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        while num >= 10:
            while num != 0:
                s += num % 10
                num //= 10
            num, s = s, num
        return num
