# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ansList = ListNode()

        curr = ansList
        carry = 0
        
        while l1 or l2 or carry > 0:
            
            l1Val = l1.val if l1 else None
            l2Val = l2.val if l2 else None
                                   
            if l1Val == None and l2Val == None and carry > 0:
                curr.next = ListNode(carry)
                carry = 0
                curr = curr.next            
            elif l2Val == None:
                curr.next = ListNode((l1Val + carry)%10)
                carry = (l1Val + carry)//10 
                curr = curr.next
                l1 = l1.next
            elif l1Val == None:
                curr.next = ListNode((l2Val + carry)%10)
                carry = (l2Val + carry)//10 
                curr = curr.next
                l2 = l2.next
            else:
                if (carry + l1Val + l2Val) < 10:
                    curr.next = ListNode(carry + l1Val + l2Val)
                    carry = 0
                
                else:
                    curr.next = ListNode((carry + l1Val+l2Val) % 10)
                    carry = (carry + l1Val+l2Val)//10
                curr = curr.next
                l1 = l1.next
                l2 = l2.next
               
        head = ansList
        ansList = head.next
        return ansList        
            
                
                
        
        
        
        