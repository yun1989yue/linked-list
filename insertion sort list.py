'''
Sort a linked list using insertion sort.
'''
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-float('Inf'))
        current = dummy
        dummy.next = head
        while current.next:
            if current.val < current.next.val:
                current = current.next
            else:
                temp = dummy
                while temp.next.val < current.next.val:
                    temp = temp.next
                exchange = current.next
                current.next = current.next.next
                exchange.next = temp.next
                temp.next = exchange
        return dummy.next
