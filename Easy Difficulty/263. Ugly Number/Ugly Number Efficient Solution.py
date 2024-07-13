class Solution:
    def isUgly(self, n: int) -> bool:
        for div in [2, 3, 5]:
            while n % div == 0 and n != 0:
                n //= div
        return n == 1
