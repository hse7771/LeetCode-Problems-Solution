class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = False
        if not s:
            return 0
        if s[0] in "+-":
            if s[0] == "-":
                sign = True
            s = s[1:]
        n = ""
        for digit in s:
            if digit.isdigit():
                n += digit
            else:
                break
        n = n or 0
        n = int(n)
        if sign:
            n *= -1
        if n > 2**31 - 1:
            return 2**31 - 1
        if n < -2**31:
            return -2**31
        return n
