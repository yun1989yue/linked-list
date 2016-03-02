'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = head
        fast = head.next
        while fast and fast.next: # find middle node
            slow = slow.next
            fast = fast.next.next
        current = slow.next
        slow.next = None
        pre = None
        while current: # reverse latter half list
            temp = current
            current = current.next
            temp.next = pre
            pre = temp
        temp = head
        while pre: # compare palindrome
            if pre.val != temp.val:
                return False
            pre = pre.next
            temp = temp.next
        return True
        
'''
if O(n) space used, we can use stack
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        stack = [head.val]
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            stack.append(slow.val)
            fast = fast.next.next
        if not fast:
            stack.pop()
        temp = slow.next
        while temp:
            key = stack.pop()
            if key != temp.val:
                return False
            temp = temp.next
        return True
