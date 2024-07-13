class Solution:
    def climbStairs(self, n: int) -> int:
        step2, step1 = 1, 1
        for i in range(2, n + 1):
            step2, step1 = step1, (step1 + step2)
        return step1
