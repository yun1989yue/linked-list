'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the 
first two lists.
'''
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        '''
        Method: Brute Force
        Complexity: O(m+n) time O(1) space
        '''
        dummy = ListNode(-1)
        temp = dummy
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
            elif l1: # if not l2, add l1 to the end of res
                temp.next = l1
                l1 = None
            else:
                temp.next = l2
                l2 = None
            temp = temp.next
        return dummy.next
        
        '''
        Method: recursion
        Complexity: O(m+n) time O(m+n) space
        '''
        if l1 and l2:
            head = l1 if l1.val < l2.val else l2
            head.next = self.mergeTwoLists(l1.next if l1.val < l2.val else l1, l2.next if l1.val >= l2.val else l2)
            return head
        elif l1 or l2:
            return l1 if l1 else l2
        else:
            return None
        
        '''
        concise recursion code
        '''
        if l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
        else:
            return l1 if l1 else l2
