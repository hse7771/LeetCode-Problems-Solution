class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        length_p = length
        for i in range(len(s)):
            if s[i] == " ":
                if length:
                    length_p = length
                length = -1
            length += 1
        return length or length_p
