'''
Reverse a singly linked list.
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None # previous node of current node
        cur = head # current node
        while cur: # reversement
            temp = cur 
            cur = cur.next
            temp.next = pre
            pre = temp
        return pre
        
