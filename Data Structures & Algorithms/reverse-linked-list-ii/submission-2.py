# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count=1
        head1=head
        prev=None
        while(head1!=None):
            if count==left:
                break
            else:
                count=count+1
                prev=head1
                head1=head1.next
        prev1=None
        new=head1
        while (count<right):
            count=count+1
            cu=head1.next
            head1.next=prev1
            prev1=head1
            head1=cu
        cu=head1.next
        head1.next=prev1
        if prev !=None:
            prev.next=head1
        new.next=cu
        if prev!=None:
            return head
        else:
            return head1


        

