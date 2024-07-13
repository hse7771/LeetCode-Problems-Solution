from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        mn_str = min(strs, key=len)
        for i in range(len(mn_str)):
            for el in strs:
                if mn_str[i] != el[i]:
                    return common_prefix
            common_prefix += mn_str[i]
        return common_prefix
