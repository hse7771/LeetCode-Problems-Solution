# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is sufficient to find the element need to be removed in the linked list and reconnect appropriate nodes.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Find the length of the list.
2. Find the node to remove calculating the index using the length of the list.
3. Remove the node making appropriate node reconnections.
4. Return the new head.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of nodes, as it is sufficient to find the length and then the element need to be removed, that demands no more than $2N$ iterations.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the number of nodes, to store the linked list.

# Code
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if length == 1 and n == 1:
            return
        if length == n:
            return head.next
        current = head
        current_i = 0
        while current.next and current_i != length - n - 1:
            current = current.next
            current_i += 1
        current.next = current.next.next
        return head 
```