'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        Head = ListNode(head.val-1)
        temp = Head
        Head.next = head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return Head.next

'''
Simplify
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current and current.next: # boundary cases considered, and must verify current exists, for input [1,1] u will get None 
            while current.next and current.val == current.next.val: # verify exists of current.next
                current.next = current.next.next
            current = current.next
        return head
