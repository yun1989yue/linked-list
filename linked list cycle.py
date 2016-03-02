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

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.
Follow up:
Can you solve it without using extra space?
'''
'''
Method 1: for each explored node, point it to itself, if cur.next.next == cur.next, we found it(cur.next)
'''
'''
Method 2: slow fast pointers
1) find the 1st node they meet
2) slow start from begining, fast from meet node, forward with same spd, and the node they meet will be the start node
assume non loop contains m nodes, loop contains n nodes, when they 1st meet, slow moves m + x nodes, then 2(m+x) = m + x + an, hence 
m + x = an, if fast moves an - x nodes with same spd as slow, it will reach the start node
'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        meet = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = slow
                break
        if not meet:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
