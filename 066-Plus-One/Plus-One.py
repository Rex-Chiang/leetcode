class Solution:
    def plusOne1(self, digits):
        # digits為[9]的情況
        if digits[0] == 9 and len(digits) == 1:
            return [1, 0]
        # digits尾數 < 9的情況(不進位)
        elif digits[-1] != 9:
            digits[-1] += 1
            return digits
        # digits尾數 >= 9的情況(進位)
        else:
            for i in range(len(digits)-1, 0, -1):
                if digits[i] >= 9:
                    digits[i] = 0
                    digits[i-1] += 1
                # 進位後若不需再進位則break
                if digits[i-1] < 10:
                    break
            # 進位後若首項為10則調整
            if digits[0] == 10:
                digits[0] = 1
                digits.append(0)                
        return digits

    def plusOne2(self, digits):
        length = len(digits) - 1
        #　先掃描並調整需進位者為0
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        # 進位至首項若為0則調整
        if(length < 0):
            digits = [1] + digits
        # 若不須進位則直接 +1
        else:
            digits[length] += 1
        return digits


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne1(digits = [1,2,3]))
    print(s.plusOne1(digits = [9]))
    print(s.plusOne1(digits = [2,4,9,3,9]))
    print(s.plusOne1(digits = [9, 9, 9]))
    print(s.plusOne1(digits = [8, 9, 9]))
    