from typing import Optional


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
