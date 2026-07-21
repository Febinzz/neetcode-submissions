# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1=l1
        head2=l2
        head3=ListNode(0)
        dummy=head3
        curr1=head1
        curr2=head2
        s1=""
        s2=""
        z=0
        while(curr1):
            s1=str(curr1.val)+s1
            curr1=curr1.next
        while(curr2):
            s2=str(curr2.val)+s2
            curr2=curr2.next
        print(s1,s2)
        x=((int(s1)+int(s2)))
        print(x)
        if x==0:
            dummy.next=ListNode(0)
            dummy=dummy.next
            return head3.next
        while(x!=0):
            y=x%10
            dummy.next=ListNode(y)
            dummy=dummy.next
            x=x//10
        return head3.next

    

            