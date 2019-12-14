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
        # tmp用以截斷重複元素
        cur = head
        tmp = dummy
        
        while cur.next != None:
            # 遇到相同則進迴圈不斷跳過
            if cur.val == cur.next.val:
                while (cur.val == cur.next.val):
                    cur = cur.next
                    # 避免 cur.next已為 None還呼叫 val(Line 22)
                    if cur.next == None:
                        break
                # 截斷重複元素
                tmp.next = cur.next
                # cur繼續往下遍尋
                cur = cur.next
            else:
                # tmp、cur繼續往下遍尋
                cur = cur.next
                tmp = tmp.next
            # 避免 cur已為 None還呼叫 next(Line 19)
            if cur == None:
                break
                
        return dummy.next
        