package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
	var slow, fast *ListNode = head, head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	second := slow.Next
	var prev *ListNode = nil
	slow.Next = nil

	for second != nil {
		var temp *ListNode = second.Next
		second.Next = prev
		prev = second
		second = temp
	}

	var first *ListNode = head
	second = prev

	for second != nil {
		var temp1 *ListNode = first.Next
		var temp2 *ListNode = second.Next

		first.Next = second
		second.Next = temp1

		first = temp1
		second = temp2
	}
}
