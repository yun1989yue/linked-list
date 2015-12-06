'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
'''
Method 1: use hashtable O(n) time O(n) space
put every explored node into it, if current node exists in hashtable, return True
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        explored = {}
        cur = head
        while cur:
            if cur not in explored: # different nodes may have same value
                explored[cur] = cur.val
            else:
                return True
            cur = cur.next # need to update the node
        return False
'''
Method 2: slow fast pointers
slow pointer moves 1 node forward each time, fast moves 2, if they meet with each other, return True
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
