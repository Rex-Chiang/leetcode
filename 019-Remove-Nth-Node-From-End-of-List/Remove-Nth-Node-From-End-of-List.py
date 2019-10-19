# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd1(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        #　計算串列總長度
        while first != None:
            length += 1
            first = first.next
            
        length = length-n
        first = dummy
        # length-n 遍尋
        while length>0:
            length -= 1
            first = first.next
            
        first.next = first.next.next
        
        return dummy.next
    
    def removeNthFromEnd2(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        # first先跑 n
        for i in range(0, n+1):
            first = first.next
        # first再跑至 null
        # second同時跑至定點
        # 由於兩者總長度相同因此可得指定點
        while first != None:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next
    