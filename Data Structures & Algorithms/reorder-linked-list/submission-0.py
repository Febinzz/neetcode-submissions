# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next=None
        prev=None
        while(curr):
            new=curr.next
            curr.next=prev
            prev=curr
            curr=new
        head1=head
        head2=prev
        while(head2):
            temp1=head1.next
            temp2=head2.next
            head1.next=head2
            head2.next=temp1
            head1=temp1
            head2=temp2
        return 
        

       