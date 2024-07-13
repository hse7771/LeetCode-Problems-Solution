class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        relevance = {}
        for i in range(len(s)):
            if s[i] not in relevance:
                if t[i] in relevance.values():
                    return False
                relevance[s[i]] = t[i]
            else:
                if relevance[s[i]] != t[i]:
                    return False
        return True
