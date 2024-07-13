# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Remember about DFS or BFS.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Implement DFS.
2. Apply min counting modification.
3. Remember about leaf condition of both children equal to null.
4. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of nodes, as it is needed to go through each node to complete the algorithm.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is also $O(N)$, where $N$ is the number of nodes, to store the tree.

# Code
```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left is None and right is None:
            return 1
        return 1 + min(left, right) if left != 0 and right != 0 else 1 + max(left, right)
            
       
```