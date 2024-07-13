# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Use DFS algorithm to solve the problem:
If the depth of left and right branches are known, than the current depth is maximum of them and one more (the current level).

# Approach
<!-- Describe your approach to solving the problem. -->
1. Implement recursive DFS algorithm.
2. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of nodes, as it is necessary to visit each node.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the number of nodes, for the worst case, in which tree is just one branch. If the tree is relatievly balanced, time complexity will be $O(H)$, where $H$ is the height of the tree, that is calculated as $logN$.

# Code
```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(Solution.maxDepth(Solution, root.left) + 1, Solution.maxDepth(Solution, root.right) + 1) 
```