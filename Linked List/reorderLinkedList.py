# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        # [0, n-1, 1, n-2, 2, n-3, ...]
        
        # find the middle of the linked list
        # to partition them
        mid = end = head
        while end and end.next:
            mid = mid.next
            end = end.next.next

        print(head, mid, end)

