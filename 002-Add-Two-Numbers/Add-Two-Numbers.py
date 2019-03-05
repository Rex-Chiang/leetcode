class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        # dummy為一啞節點(dummy node)
        dummy = ListNode(0)
        # dummy = dummy       ---> out.next    ---> out.next    ---> out.next
        # dummy = ListNode(0) ---> ListNode(7) ---> ListNode(0) ---> ListNode(1+7)
        out = dummy # 串接"動作"
        carry = 0
        while l1 or l2 or carry:
            # 在此做了進位動作
            sum, carry = carry, 0
            
            if l1 != None:
                sum += l1.val
                l1 = l1.next
                
            if l2 != None:
                sum += l2.val
                l2 = l2.next
                
            if sum > 9:
                carry = 1
                sum -= 10
            # 建構pointer
            out.next = ListNode(sum)
            # 串接"動作",表示只有目前這段的狀態
            out = out.next
        return dummy.next


if __name__ == "__main__":
    
    s = Solution
    
    l1 = [2,4,3]
    l2 = [5,6,4]
    
    l1 = ListNode(l1[0])
    l2 = ListNode(l2[0])
    
    print(s.addTwoNumbers(s,l1,l2).val)