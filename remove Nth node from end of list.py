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
