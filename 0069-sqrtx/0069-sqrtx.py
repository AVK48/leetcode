class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 2, x // 2
        ans = 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            n = m * m
            
            if n == x:
                return m  
            elif n < x:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans 