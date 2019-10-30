# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # We first create a new and stable listnode, which always points
        # at the head of listnode.
        dummy = ListNode(None)
        
        # Then we create a temporary listnode, this temporary listnode will finally
        # point at the tail of the listnode.
        temp = dummy
        
        # For normal cases (both l1 and l2 are not empty)
        while l1 and l2:
            # step forward 
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
                
            temp = temp.next
            
        # For special case (either l1 or l2 is emply)
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        
        # Both 'dummy' and 'temp' are listnodes, since they point at different
        # indices of the same listnode, we always return 'dummy' since it's the 
        # head of the listnode, which represents the whole listnode.
        if dummy.val == None:
            dummy = dummy.next
        
        return dummy
                
        
        