'''
 linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
'''
'''
Use Hashtable, O(n) time O(n) space
1) For each next node, if it is not created, create it(if u wanna complete the copy in one time, u may create the next node before
becasue of random pointer)
2) For each random node, same
3) HashTable example (label, node)
'''
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        dic = {}
        dummy = RandomListNode(0) 
        temp = dummy
        while head: 
            if head.label in dic:
                temp.next = dic[head.label]
            else:
                temp.next = RandomListNode(head.label)
                dic[head.label] = temp.next
            if head.random == None:
                temp.next.random = None
            else:
                if head.random.label in dic:
                    temp.next.random = dic[head.random.label]
                else:
                    temp.next.random = RandomListNode(head.random.label)
                    dic[head.random.label] = temp.next.random
            head = head.next
            temp = temp.next
        return dummy.next
