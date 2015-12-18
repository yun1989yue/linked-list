'''
Given a linked list, swap every two adjacent nodes and return its head. 

For example,
 Given 1->2->3->4, you should return the list as 2->1->4->3. 

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 

'''
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        '''
        Method: Brute Froce
        Complexity: O(n) time O(1) space
        '''
        dummy = ListNode(-1) # head may be changed
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next: 
            temp = cur
            cur = cur.next
            temp.next = cur.next
            cur.next = cur.next.next
            temp.next.next = cur
        return dummy.next
        
        '''
        Method: Recursion
        Complexity: O(n) time O(n) space
        '''
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next = head
        return temp
