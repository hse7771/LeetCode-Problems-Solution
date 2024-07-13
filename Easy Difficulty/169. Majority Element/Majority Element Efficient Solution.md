# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
There are several approaches to solve the problem efficiently.
The most obvious one probably is to use the hash table to count each occurence of the numbers in the array and then find the number with the highest frequency.
It will have $O(N)$ time complexity and $O(K)$ space complexity, where $N$ is the number of elements in the array and $K$ is the number of unique elements.
Please refer for this solution to:\
https://leetcode.com/problems/majority-element/submissions/1247203890

# Approach
<!-- Describe your approach to solving the problem. -->
The approach represented further is use of Boyer-Moore Voting Algorithm. It is possible to use it, as there is a condition of existence element with frequency higher than $N/2$.
The key idea of the algorithm is that if there is an element with $N/2$ frequency it is guaranteed that the count will have non-zero value at the end and the element would be found.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, as no more than $N$ iterations are performed to complete the algorithm execution.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity becomes $O(1)$, as no extra space is needed.

# Code
```
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 0, None
        for number in nums:
            if count == 0:
                majority = number
                count += 1
            elif number == majority:
                count += 1
            else:
                count -= 1
        return majority

```