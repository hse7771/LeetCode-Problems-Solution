# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To merge sorted array in place it is possible to start merging from the end.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Merge arrays gradually starting from the end.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the result array, as no more than $N$ merging operations may be performed.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the result array, to store the result array.

# Code
```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n != 0:
            if m == 0 or nums2[n-1] >= nums1[m-1]:
                nums1[n+m-1] = nums2[n-1]
                n -= 1
            else:
                nums1[n+m-1] = nums1[m-1]
                nums1[m-1] = 0
                m -= 1
```