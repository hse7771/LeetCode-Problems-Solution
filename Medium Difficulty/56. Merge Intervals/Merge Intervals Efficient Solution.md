# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The initial idea that comes to mind is to union appropriate intervals in some smart way. However, how can it be achieved? Comparing only adjacent elements is not sufficient to get all necessary intervals to be merged at the end, as they can be divided by some other elements.
It is possible to make two loops to fix it, but it gives quadratic asymptotic and slows the program critically.

# Approach
<!-- Describe your approach to solving the problem. -->
The right way to improve the efficiency is to sort the intervals before comparing adjacent elements. It lets achieve better performance and makes adjacent element comparing sufficient to get correct result.
1. Sort the intervals.
2. Compare the adjacent intervals, removing redundant element if necessary.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(NlogN)$, because of sorting operation use. It makes it possible to complete the algorithm only using one loop after this sorting.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the number of intervals to be merged, to store these intervals and all other operations are performed in place.

# Code
```


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
```