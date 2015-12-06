'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow = head
        fast = head
        while fast and fast.next: # find middle node
            slow = slow.next
            fast = fast.next.next
        pre = None
        current = slow.next # slow may not exists
        slow.next = None
        while current: reverse latter half list
            temp = current
            current = current.next
            temp.next = pre
            pre = temp
        pos = head
        neg = pre
        while neg:
            temp = neg
            neg = neg.next
            temp.next = pos.next
            pos.next = temp
            pos = temp.next
