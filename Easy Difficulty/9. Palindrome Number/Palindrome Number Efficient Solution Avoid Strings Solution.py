class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        length = 1
        while x // 10 ** length != 0:
            length += 1
        i = 0
        while i < length // 2:
            if (x // 10 ** (length - 1 - i)) % 10 != x // 10 ** i % 10:
                return False
            i += 1
        return True
