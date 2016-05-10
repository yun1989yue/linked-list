Method:
1) Brute Force
Add Two Numbers, Merge Two Sorted Lists, Swap Nodes in Pairs, Reverse Nodes in k-Group, Remove Duplicates from Sorted List
Remove Duplicates from Sorted List II, Partition List, Reverse Linked List, Reverse Linked List II, Insertion Sort List
Remove Linked List Elements, Reverse Linked List
2) two pointers:
  2-1) slow-fast: find middle node, or check circulation
  Convert Sorted List to Binary Search Tree, Linked List Cycle, Linked List Cycle II, Reorder List, Sort List, Palindrome Linked List
  2-2) same difference
  Remove Nth Node From End of List, Rotate List
3) recursion
Reverse Nodes in k-Group
4) heap
Merge k Sorted Lists
5) math
Linked List Cycle II, Intersection of Two Linked Lists
6) dictionary
Copy List with Random Pointer

Error:
1) dummy node needs to judge whether to connect to head or not
2) temp node needs to judge whether to update or not
3) check whether node exists before calling its val or next
4) careful about rotation, if rotate k times, k maybe longer than length l of list, need to find k%l 
5) careful about possible loops created by wrong or missed updation

skills:
1) dummy node can clarify the code if the head of res is not determined

Boundary Case:
1) not head
2) not head.next
