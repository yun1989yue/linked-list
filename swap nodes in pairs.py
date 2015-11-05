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
        tempHead = ListNode(-1)
        previous = tempHead
        tempHead.next = head
        current = head
        while current and current.next:
            previous.next = current.next
            current.next = previous.next.next
            previous.next.next = current
            previous = current
            current = current.next
        return tempHead.next
