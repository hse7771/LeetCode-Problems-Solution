# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It is necessary to find new head-tail of the linked list after rotation to efficiently update them for $O(1)$ and complete the problem solving. However, there is a need to know the length of the linked list before finding operation, therefore, it should be calculated first.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Calculate the length of the linked list.
2. Using two pointers, find new tail-head of rotated list.
3. Perform reassigning of head and tail pointers.
4. Return the new head.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of nodes and no more than $2N$ iterations are needed to solve the problem.

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        if length == 0:
            return 
        k %= length

        tail, new_tail = head, head
        count = 0
        while tail:
            if tail.next is None:
                break
            else:
                count += 1
                tail = tail.next
                if count == k + 1:
                    new_tail = new_tail.next
                    count = k
        tail.next = head
        head = new_tail.next
        new_tail.next = None
        return head
```