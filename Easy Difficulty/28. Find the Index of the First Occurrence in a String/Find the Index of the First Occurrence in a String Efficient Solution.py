class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            fl = False
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    fl = True
                    break
            if fl:
                continue
            return i
        return -1
