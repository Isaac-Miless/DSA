# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: 'Optional[ListNode]', n: int) -> 'Optional[ListNode]':
        length = 0
        first = head
        
        while first:
            length += 1
            first = first.next
        
        if length == n:
            return head.next
        
        currNode = 1
        first = head
        while first and currNode < length - n:
            first = first.next
            currNode += 1

        if first and first.next:
            first.next = first.next.next

        return head
