# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution:
    def mergeTwoLists(self, l1, l2):
        tmp = ListNode(0)
        # 因tmp會移動，因此需dummy指向
        dummy = ListNode(0)
        dummy.next = tmp
        
        first1 = l1
        first2 = l2
        # 由first1及first2分別遍尋兩串列
        # tmp再依大小串接
        while (first1 != None) and (first2 != None):
            
            if first1.val <= first2.val:
                tmp.next = first1
                first1 = first1.next
                
            else:
                tmp.next = first2
                first2 = first2.next
                
            tmp = tmp.next
        # 若兩串列其中有None出現，則直接串接非None串列
        tmp.next = first1 or first2
        
        return dummy.next.next
                