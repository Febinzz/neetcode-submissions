"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head1=Node(0)
        curr1=head1
        curr=head
        a={}
        while(curr):
            curr1.next=Node(curr.val)
            a[curr]=curr1.next
            curr1=curr1.next
            curr=curr.next
        curr=head
        curr1=head1.next
        while curr1 and curr:
            if curr.random:
                curr1.random=a[curr.random]
            curr=curr.next
            curr1=curr1.next
        return head1.next

        