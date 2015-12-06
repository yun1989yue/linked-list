'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
'''
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        tempHead = ListNode(0)
        tempHead.next = head
        start = tempHead
        for i in xrange(m-1): # find m-1th node
            start = start.next
        pre = start.next
        cur = pre.next
        for i in xrange(n-m): # reverse nodes from m to n
            temp = cur
            cur = cur.next
            temp.next = pre
            pre = temp
        start.next.next = cur # connect with edge nodes
        start.next = pre
        return tempHead.next
