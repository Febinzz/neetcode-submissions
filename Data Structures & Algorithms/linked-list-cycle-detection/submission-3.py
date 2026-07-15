# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1=head
        curr2=head
        if head==None:
            return False
        while curr1.next!=None and curr2.next!=None and  curr2.next.next!=None:
            if curr1.next==curr2.next.next:
                return True
            else:
                curr1=curr1.next
                curr2=curr2.next.next
        return False