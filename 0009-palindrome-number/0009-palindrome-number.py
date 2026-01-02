class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        rev = 0
        sign = -1 if x < 0 else 1
        a = x
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Overflow check BEFORE update
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return False
            if a<0:
                return False

            rev = rev * 10 + digit
        if a==rev:
            return True
        else:
            return False

         

