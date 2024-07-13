class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        s = list(s)
        while i <= len(s)-2:
            if s[i].lower() == s[i+1].lower() and s[i] != s[i+1]:
                s.pop(i)
                s.pop(i)
                i = max((i-1), 0)
                continue
            i += 1
        return "".join(s)
