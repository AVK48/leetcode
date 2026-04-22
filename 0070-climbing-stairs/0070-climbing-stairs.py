class Solution:
    def climbStairs(self, n: int) -> int:
        v,p = 1,1
        for i in range(n-1):
            
            v,p = v+p, v
        return v