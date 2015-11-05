class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2): 
        ''' 
        Method: two pointers with difference n 
        Complexity: O(m+n) time O(1) space 
        '''
        carry = 0
        temphead = ListNode(-1)#tempHead is convenient when the head of res is not determined 
        temp = temphead
        t1 = l1#use reference to save original linked lists
        t2 = l2
        while t1 or t2 or carry:
            Sum = 0
            if t1:
                Sum += t1.val
                t1 = t1.next
            if t2:
                Sum += t2.val
                t2 = t2.next
            Sum += carry
            carry = Sum / 10
            Sum %= 10
            temp.next = ListNode(Sum)
            temp = temp.next
        return temphead.next
