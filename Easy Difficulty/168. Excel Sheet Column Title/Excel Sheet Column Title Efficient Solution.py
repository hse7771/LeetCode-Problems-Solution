class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_title = ""
        correction = 64
        base = 26
        while columnNumber != 0:
            if columnNumber % base == 0:
                column_title += chr(base + correction)
                columnNumber //= base
                columnNumber -= 1
            else:
                column_title += chr(columnNumber % base + correction)
                columnNumber //= base
        return column_title[::-1]
