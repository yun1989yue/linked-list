'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''
'''
Method 1:
1) find length of two linked lists l1, l2(assume l2 greater)
2) set two pointers at beginning of each list and move longer one forward l2 - l1 steps
3) find intersection
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = 0
        l2 = 0
        tA = headA
        tB = headB
        while tA:
            l1 += 1
            tA = tA.next
        while tB:
            l2 += 1
            tB = tB.next
        if l1 < l2:
            return self.helper(headA, headB, l1, l2)
        else:
            return self.helper(headB, headA, l2, l1)
        
    def helper(self, headA, headB, l1, l2):
        tA = headA
        tB = headB
        while l2 != l1:
            tB = tB.next
            l2 -= 1
        while tA and tA != tB:
            tA = tA.next
            tB = tB.next
        return tA
        
'''
Method 2:
1) two pointers start from each list
2) if a list has been explored, move its pointer to the beginning of the other list
* no need to set flag, two pointers will meet either they refer to the same node or null
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tA = headA
        tB = headB
        while tA or tB:
            if tA == tB:
                return tA
            if not tA:
                tA = headB
            else:
                tA = tA.next
            if not tB:
                tB = headA
            else:
                tB = tB.next
