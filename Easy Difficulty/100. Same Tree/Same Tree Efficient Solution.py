from typing import Optional


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
