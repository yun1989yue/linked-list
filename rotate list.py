'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k): # notice that k may be larger than length of list
        if not head or not head.next:
            return head
        temp = head
        l = 0
        while temp: # find length of list
            l += 1
            temp = temp.next
        k %= l
        if k == 0: 
            return head
        end = head
        for i in xrange(k):
            end = end.next
        start = head
        while end.next:
            end = end.next
            start = start.next
        Head = start.next
        start.next = None
        end.next = head
        return Head
