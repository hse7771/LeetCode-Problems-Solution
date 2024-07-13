# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Classic use of Binary Search algorithm.
# Approach
<!-- Describe your approach to solving the problem. -->
As all elements are sorted, it is possible to use Binary Search algorithm.
1. Initialize left and right borders.
2. Calculate the middle element.
3. Reduce by half the number of elements to be considered in the loop until either the target is found or its potential place.
4. Return the appropriate index.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $logN$ as it is Binary Search algorithm time complexity. There will be less than $logN$ comparisons done as after each of them the number of potential elements to compare reduces by a factor of $2$.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the number of elements.

# Code
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while right - left != 1:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle
        return right
```