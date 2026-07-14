# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        curr1=head1
        curr2=head2
        head3=ListNode(0)
        curr3=head3
        while(curr1!=None and curr2!=None):
            if curr1.val<=curr2.val:
                curr3.next=curr1
                curr3=curr3.next
                curr1=curr1.next
            else:
                curr3.next=curr2
                curr3=curr3.next
                curr2=curr2.next
        if curr1!=None:
            while(curr1.next!=None):
                curr3.next=curr1
                curr3=curr3.next
                curr1=curr1.next
            curr3.next=curr1
            curr3=curr3.next
        if curr2!=None:
            while(curr2.next!=None):
                curr3.next=curr2
                curr3=curr3.next
                curr2=curr2.next
            curr3.next=curr2
            curr3=curr3.next
        curr3.next=None
        return head3.next
        

