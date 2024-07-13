from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            prev, cur = intervals[i-1], intervals[i]
            mn_begin, mx_begin = min(prev[0], cur[0]), max(prev[0], cur[0])
            mn_end, mx_end = min(prev[1], cur[1]), max(prev[1], cur[1])
            if mn_begin <= mx_begin <= mn_end <= mx_end:
                interval = [mn_begin, mx_end]
                intervals[i] = interval
                intervals.pop(i-1)
            else:
                i += 1
        return intervals
