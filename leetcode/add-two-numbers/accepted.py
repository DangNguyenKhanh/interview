# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head node to simplify edge cases for list construction
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Loop until both lists are fully traversed AND no carry remains
        while l1 or l2 or carry:
            # Get values from current nodes (or 0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create a new node with the digit and attach to result list
            curr.next = ListNode(digit)
            curr = curr.next

            # Move to the next nodes in input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the actual head of the resulting linked list (skip dummy)
        return dummy.next
