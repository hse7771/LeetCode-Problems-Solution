# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To solve the problem it is necessary to find left and right bounds of the target element. The best way to perform this task in the sorted array is to use binary search algorithm.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Find the left bound of the target using binary search algorithm.
2. Reassign start values for range to be searched according to the found left boundary.
3. Find the right bound of the target using binary search algorithm.
4. Return target boundaries.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(logN)$, as it is binary search algorithm time complexity.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the list, to store it.

# Code
```
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        positions = [-1, -1]
        left, right = -1, len(nums)
        if nums:
            while right - left != 1:
                middle = (left + right) // 2
                if nums[middle] >= target:
                    right = middle
                else:
                    left = middle
            if right < len(nums) and nums[right] == target:
                positions[0] = right
            left, right = right-1, len(nums)
            while right - left != 1:
                middle = (left + right) // 2
                if nums[middle] <= target:
                    left = middle
                else:
                    right = middle
            if nums[left] == target:
                positions[1] = left
        return positions
```