# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is necessary to reconnect several appropriate nodes on each iteration to implement the proper change.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Perform head change separately.
2. Change all other elements in the list.
3. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of nodes, as it is necessary to perfrom around $N/2$ changes.

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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if head is None or head.next is None:
            return head
        tmp = current.next
        current.next = tmp.next
        tmp.next = current
        head = tmp
        while current and current.next and current.next.next:
            tmp = current.next
            current.next = tmp.next
            tmp.next = current.next.next
            current.next.next = tmp
            current = current.next.next
        return head
            
```