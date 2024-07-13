# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The basic idea to solve the problem is to go from the root to all leaves and check the final sum.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Implement DFS.
2. Apply sum check modification to DFS.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of nodes, as it would be necessary to go through each node before reaching each of leaves.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the number of nodes, to store the tree.

# Code
```

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def depth_step(current, s):
            if current is None:
                return False
            s += current.val
            if current.left is None and current.right is None:
                return targetSum == s 
            return depth_step(current.left, s) or depth_step(current.right, s)
        return depth_step(root, 0)
        
```