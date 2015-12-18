'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
'''
M1: merge each two lists iteratively, need 2n + 3n + ... + kn ~ O(k^2 * n) time
'''
'''
M2: each time compare k lists and add 1 node to res, so O(k) time for kn nodes O(k^2 * n) time
'''
''' 
M3: Heap O(kn) time O(k) space
'''
from heapq import heappush,heappop,heapify
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(n.val,n) for n in lists if n] #put the head of each list into heap
        heapify(heap) # tranform list to heap by O(n) time
        tempHead = ListNode(0)
        temp = tempHead
        while heap:
            val,node = heappop(heap) # pop 1st(smallest) elem of heap
            if node.next:
                heappush(heap,(node.next.val,node.next)) # push an elem into heap
            temp.next = node
            temp = temp.next
        return tempHead.next
