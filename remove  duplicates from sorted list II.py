'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(head.val - 1)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                explore = current.next.val
                while current.next and current.next.val == explore:
                    current.next = current.next.next
            else:
                current = current.next
        return dummy.next
        
  '''
  recursion
  '''
  class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            key = head.val
            while head and head.val == key:
                head = head.next
            res = self.deleteDuplicates(head)
            return res
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
