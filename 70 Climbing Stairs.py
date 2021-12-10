# https://leetcode.com/problems/climbing-stairs/

def fibo(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))

# just need to find the factorial 
class Solution:
    def climbStairs(self, n: int) -> int:
        return fibo(n+1)
