# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        
        l1Val = l1.val if l1 else None
        l2Val = l2.val if l2 else None
        
        if l1Val == None and l2Val == None:
            return
        
        elif l1Val == None:
            dummyHead = ListNode(l2Val)
            curr = dummyHead
            l2 = l2.next
        elif l2Val == None:
            dummyHead = ListNode(l1Val)
            curr = dummyHead
            l1 = l1.next
            
        elif l1Val <= l2Val:
            dummyHead = ListNode(l1Val)
            curr = dummyHead
            l1 = l1.next
        else:
            dummyHead = ListNode(l2Val)
            curr = dummyHead
            l2 = l2.next
            
        
        while l1 or l2:
            l1Val = l1.val if l1 else None
            l2Val = l2.val if l2 else None
            
            if l2Val == None:
                curr.next = ListNode(l1Val)
                curr = curr.next
                l1 = l1.next
            elif l1Val == None:
                curr.next = ListNode(l2Val)
                curr = curr.next
                l2 = l2.next
            elif l1Val == None and l2Val == None:
                return dummyHead
            elif l1Val <= l2Val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
            
        return dummyHead
                
        