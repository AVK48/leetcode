# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Continue as long as there are nodes to process or a carry left over
        while l1 or l2 or carry:
            # Get the value from each list, or 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Create a new node with the result and move the pointer
            current.next = ListNode(new_val)
            current = current.next
            
            # Advance l1 and l2 if they aren't null
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
        