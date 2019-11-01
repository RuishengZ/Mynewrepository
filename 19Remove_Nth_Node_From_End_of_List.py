# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # In this problem, we will use two "pointers": "fast" and "slow"
        # in order to find the n-th node from the end of list. "fast" pointer
        # go n+1 steps first, then the "slow" pointer will follow. An inverval 
        # is formed by using this method, the length of this interval is n + 1
        # and this interval is the key to find the required node.
        origin = ListNode(0)
        fast = origin
        slow = origin
        origin.next = head
        
        # "Fast" pointer will move forward first.
        for i in range(n + 1):
            fast = fast.next
        
        # "slow" pointer starts moving, together with "fast", until
        # the "fast" pointer points to None.
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return origin.next
        