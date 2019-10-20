# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution:
    def swapPairs1(self, head):
        # 空集合或只有單一元素的狀況
        if not head or not head.next: 
            return head
        
        dummy = tmp = ListNode(0)
        tmp.next = head
        # 利用3個指標遍尋互換
        while tmp.next and tmp.next.next:
            first = tmp.next
            sec = tmp.next.next
            
            tmp.next = sec
            first.next = sec.next
            sec.next = first
            
            tmp = tmp.next.next
            
        return dummy.next
    
    def swapPairs2(self, head):
        # 空集合或只有單一元素的狀況
        if not head or not head.next: 
            return head
        # 以遞歸進行互換，每次遞歸回傳未被指向的那個節點
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            
            return tmp
        
        return head
                