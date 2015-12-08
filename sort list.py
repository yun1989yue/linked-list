'''
Sort a linked list in O(n log n) time using constant space complexity.
'''
'''
Method: divide and conquer O(nlogn) time O(n) space
'''
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next: # find middle node
            slow = slow.next
            fast = fast.next.next
        latter = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(latter)
        return self.comb(left, right)
    
    def comb(self, left, right): # sort the sublist
        dummy = ListNode(min(left.val, right.val) - 1)
        current = dummy
        while left or right:
            if not left:
                current.next = right
                break
            if not right:
                current.next = left
                break
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        return dummy.next
