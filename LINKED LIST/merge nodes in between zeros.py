# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        c=dummy
        while c.next:
            p=c
            if c.next.val==0:
                c=c.next
            if c.next:
                c.val+=c.next.val
                c.next=c.next.next
        p.next=None
        return head
        

        