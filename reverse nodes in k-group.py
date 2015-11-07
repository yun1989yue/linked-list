'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or not head.next or k == 1:
            return head
        temp = head
        l = 0
        while temp: # length of list
            l += 1
            temp = temp.next
        times = l/k
        tempHead = ListNode(0)
        tempHead.next = head
        start = tempHead
        pre = tempHead
        cur = head
        for i in xrange(times): # for each k elems, reverse it
            for j in xrange(k):
                temp = cur
                cur = cur.next
                temp.next = pre
                pre = temp
            pre = start.next # connect local head and tail
            start.next = temp
            pre.next = cur
            start = pre
        return tempHead.next
'''
recursion
'''
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 1:
            return head
        temp = head
        for i in xrange(k-1): # notice that if length of list is k, you need to reverse but next recursice node is None
            if not temp.next:
                return head
            else:
                temp = temp.next
        temp = temp.next
        previous = self.reverseKGroup(temp, k)
        current = head
        for i in xrange(k):
            temp = current
            current = current.next
            temp.next = previous
            previous = temp
        return previous
