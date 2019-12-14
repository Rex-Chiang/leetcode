# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head, x) :
        # 因 small_tmp、big_tmp會移動，需 dummy作指向
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)
        # cur用以遍尋 Linked List
        cur = head
        # small_tmp用以串接小於 x的區段
        small_tmp = small_dummy
        # big_tmp用以串接大於 x的區段
        big_tmp = big_dummy
        
        while cur != None:
            if cur.val < x:
                small_tmp.next = cur
                small_tmp = small_tmp.next
            elif cur.val >= x:
                big_tmp.next = cur
                big_tmp = big_tmp.next
                
            cur = cur.next
        # 大於 x的區段作結尾
        big_tmp.next = None
        # 以 small_tmp、big_dummy串接兩區段
        small_tmp.next = big_dummy.next
        # 以 small_dummy指向 small_tmp
        return small_dummy.next
        