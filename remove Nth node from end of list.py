'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.


Note:
 Given n will always be valid.
 Try to do this in one pass. 

'''
class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n): 
        '''
        Method: two pointers with difference n
        Complexity: O(n) time O(1) space
        '''
        if n == 0:
            return head
        tempHead = ListNode(-1)
        tempHead.next = head
        temp = tempHead
        for i in xrange(n):
            temp = temp.next
        start = tempHead
        while temp.next:
            start = start.next
            temp = temp.next
        start.next = start.next.next
        return tempHead.next
