'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
class Solution():
    def partition(self, head, x): # notice that the title requests preservation of original list
        small = ListNode(x-1)
        ts = small
        large = ListNode(x)
        tl = large
        temp = head
        while temp:
            if temp.val < x:
                ts.next = temp
                ts = ts.next
            else:
                tl.next = temp
                tl = tl.next
            temp = temp.next
        ts.next = large.next
        tl.next = None
        return small.next

'''
In-place Method
'''
class Solution():
    def partition(self, head, x):
        tempHead = ListNode(x-1)
        tempHead.next = head
        start = tempHead
        current = tempHead
        while current.next:
            if current.next.val < x and start != current:
                temp = current.next
                current.next = current.next.next
                temp.next = start.next
                start.next = temp
                start = temp # need to update start pointer
            else:
                if current.next.val < x and current == start:
                    start = start.next
                current = current.next
        return tempHead.next
            
