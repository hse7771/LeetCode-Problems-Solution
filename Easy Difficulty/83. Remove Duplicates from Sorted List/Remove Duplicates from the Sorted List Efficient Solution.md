# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
To delete duplicates in the sorted linked list, it is sufficient to check if all adjacent elements are distinct. 

# Approach
<!-- Describe your approach to solving the problem. -->
1. Iterate through the all elements checking if there are equal adjacent elements.
2. Delete all equal elements except one by attaching the unique value node to the next one until the equal elements end.
3. Return the head of the updated linked list.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the length of the linked list, as it is necessary to iterate through the all elements of it.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the length of the linked list, to store it.

# Code
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
```