# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, a: List[List[int]]) -> int:
        
        n = len(a)      # length of grid
        sum = 0         # this hold sum
        
        i = 0           # for 1st diagonal, 1st value at 0,0 top left
        j = 0           # right diagonal
        while (i < n):
            sum += a[i][j]
            i+=1
            j+=1
        
        i = 0           # left diagonal, 1st val at top right 
        j = n - 1
        while (j >= 0):
            sum += a[i][j]
            i+=1
            j-=1
        
        # if matrix is odd, we need to - middle value as it is added in both diagonals
        if (n % 2 != 0) : sum -= a[n//2][n//2]
            
        return sum
