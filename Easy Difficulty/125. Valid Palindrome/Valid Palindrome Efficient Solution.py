class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([letter for letter in s if letter.isalnum()]).lower()
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True
