# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=1
        while(curr.next!=None):
            count=count+1
            curr=curr.next
        print(count)
        val=count-n
        print(val)
        curr=head
        if val==0:
            if head.next==None:
                return None
            else:
                return head.next
        elif val!=count-1:
            x=1
            prev=curr
            curr=curr.next
            while(curr.next!=None):
                if x==val:
                    prev.next=curr.next
                    break
                else:
                    x=x+1
                    prev=curr
                    curr=curr.next  
        else:
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None
        return head




        