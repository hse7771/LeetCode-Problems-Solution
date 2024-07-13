# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Remember about the best possible data structures to check the duplicates existence.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Create an empty set.
2. Add an element if it is not already in the set.
3. Return True if the element is a duplicate.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of the elements in the array, as it is necessary to check each element for being a duplicate.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the number of the elements in the array, to store the array and the set.

# Code
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for el in nums:
            if el in elements:
                return True
            elements.add(el)
        return False
```