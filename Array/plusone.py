class Solution:
    def plusOne(self, digits):
        n = len(digits)
        i = n-1 # reverse traverse
        carry = 1 # initialize to 1 by default
        while i >= 0 and carry == 1:

            if digits[i]+carry == 10 :
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0
                break
            i -= 1
        
        if i < 0 and carry == 1:
            digits = [carry] + digits[:n]

        return digits  
 
s = Solution()
digits =[1,9,8]
print(s.plusOne(digits))

