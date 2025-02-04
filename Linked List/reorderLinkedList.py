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
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # beginning of the second half of the LL
        second = slow.next
        prev = slow.next = None # split the LL

        # reverse the second half of the LL
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two halves
        # prev = second half of the LL
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
