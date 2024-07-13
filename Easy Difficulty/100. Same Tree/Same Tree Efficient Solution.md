# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is sufficient to check the relevance between every node in trees. To do it, it is possible to use DFS or BFS with modification of checking the element relevance.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Implement DFS.
2. Apply relevance modification.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of nodes, as it would be necessary to go through each node to check if it is the same with the one in the other tree.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(current1, current2):
            if current1 is None and current2 is None:
                return True
            if current1 and current2:
                if current1.val != current2.val:
                    return False
                return dfs(current1.left, current2.left) and dfs(current1.right, current2.right)
            return False
        return dfs(p, q)
```