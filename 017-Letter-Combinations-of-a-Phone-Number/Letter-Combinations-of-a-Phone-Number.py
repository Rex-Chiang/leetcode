class Solution:
    def letterCombinations(self, digits):
        phone = {"2":"abc",
                 "3":"def",
                 "4":"ghi",
                 "5":"jkl",
                 "6":"mno",
                 "7":"pqrs",
                 "8":"tuv",
                 "9":"wxyz",}
        
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                output.append(combination)
            # if there are still digits to check
            else:
                for i in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + i, next_digits[1:])
        
        output = []
        
        if digits:
            backtrack("", digits)
        
        return output
        
        
if __name__ == "__main__":
    s = Solution()
    
    print(s.letterCombinations("23"))