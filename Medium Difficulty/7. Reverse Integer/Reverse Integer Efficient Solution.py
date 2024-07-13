class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1]
        if x[-1] == "-":
            x = "-" + x[:-1]
        return int(x) if -2**31 <= int(x) <= 2**31-1 else 0
