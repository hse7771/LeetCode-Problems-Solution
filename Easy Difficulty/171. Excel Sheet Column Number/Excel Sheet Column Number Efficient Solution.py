class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        base = 26
        length = len(columnTitle)
        for i in range(length):
            n += (ord(columnTitle[i])-64)*base**(length - i - 1)
        return n
