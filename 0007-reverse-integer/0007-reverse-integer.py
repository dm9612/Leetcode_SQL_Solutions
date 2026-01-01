class Solution:
    def reverse(self, x: int) -> int:
        n = len(str(abs(x)))
        sum = 0
        a = x

        while n>0:
            last = abs(x)%10
            x = abs(x)//10
            sum = (sum*10) + abs(last)
            n-=1
        if a<0:
            sum = -sum
        if sum>2**31 - 1 or sum< -2**31:
            return 0
        
    
        return sum