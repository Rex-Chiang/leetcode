# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        # cur用以遍尋 Linked List
        cur = head
        
        while cur.next != None:
            # 遇到相同則跳過
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                
        return dummy.next    