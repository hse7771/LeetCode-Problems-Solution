class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = {}
        cur_start = 0
        count = 0
        for i in range(len(s)):
            if s[i] not in current:
                current[s[i]] = i
            else:
                if cur_start < current[s[i]] + 1:
                    cur_start = current[s[i]] + 1
                current[s[i]] = i
            count = max(count, i - cur_start + 1)
        return count
