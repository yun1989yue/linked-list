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
