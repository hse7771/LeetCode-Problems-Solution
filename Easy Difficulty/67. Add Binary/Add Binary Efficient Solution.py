class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def intTObinary(n):
            result = ""
            if n == 0:
                return "0"
            while n != 0:
                result += str(n % 2)
                n //= 2
            return result[::-1]

        def binaryTOint(n_str):
            n = 0
            for i in range(len(n_str)):
                n += int(n_str[i]) * 2 ** (len(n_str) - i - 1)
            return n

        return intTObinary(binaryTOint(a) + binaryTOint(b))
