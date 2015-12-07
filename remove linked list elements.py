'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(val - 1)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
        
'''
2 recursion methods, but will exceed the recursion stack in python, 2nd method is interesting
'''
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        if head.val == val:
            return self.removeElements(head.next, val)
        current = head
        while current.next and current.next.val != val:
            current = current.next
        if current.next:
            current.next = self.removeElements(current.next, val)
        return head
        
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        head.next = self.removeElements(head.next, val) # make sure that every node will be checked
        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            return self.removeElements(head, val)
