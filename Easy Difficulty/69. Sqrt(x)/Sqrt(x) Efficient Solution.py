class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        while right - left != 1:
            root = (right + left) // 2
            if root*root <= x:
                left = root
            else:
                right = root
        return left
