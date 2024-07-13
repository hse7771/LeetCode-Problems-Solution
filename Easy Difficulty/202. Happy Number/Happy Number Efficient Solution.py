class Solution:
    used_numbers = set()

    def isHappy(self, n: int) -> bool:
        self.used_numbers.add(n)
        if n == 1:
            self.used_numbers.clear()
            return True
        else:
            n1 = 0
            while n != 0:
                n1 += (n % 10)*(n % 10)
                n //= 10
            if n1 in self.used_numbers:
                return False
            return Solution.isHappy(Solution, n1)
