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
        tempHead = ListNode(-1) # Boundary case, n = len(head), then 1st node will be rmed
        tempHead.next = head
        temp = tempHead
        for i in xrange(n): # move latter pointer n steps forward
            temp = temp.next
        start = tempHead
        while temp.next: # find nth node from the end
            start = start.next
            temp = temp.next
        start.next = start.next.next # delete nth node
        return tempHead.next
