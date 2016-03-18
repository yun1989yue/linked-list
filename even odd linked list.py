'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.



Example:
 Given 1->2->3->4->5->NULL,
 return 1->3->5->2->4->NULL. 

Note:
 The relative order inside both the even and odd groups should remain as it was in the input. 
 The first node is considered odd, the second node even and so on ... 
'''
'''
test cases:
None
1
1->2
1->2->3
1->2->3->4
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        even = ListNode(-1)
        dummy = even
        while odd.next and odd.next.next: # notice that if there are 2n+1 nodes, we need to make sure odd.next exists or not
            even.next = odd.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next
        even.next = None if not odd.next else odd.next # notice that if there are 2n nodes, last node need to be added, else last node in even list need to point to None
        odd.next = dummy.next
        return head
