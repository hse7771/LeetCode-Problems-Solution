# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To solve the problem, it is necessary just to remove appropriate nodes connecting previous node to the next one skipping the current node.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Find head with not value need to delete.
2. Remove all nodes with value to delete reconnecting the appropriate nodes.
3. Return the new head.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, as $N$ iterations are necessary to check all nodes and remove wrong ones, where $N$ is the number of nodes in the list.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the number of nodes in the list, to store it.

# Code
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        current = head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head
                
```