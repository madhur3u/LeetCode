// https://leetcode.com/problems/matrix-diagonal-sum/

public int diagonalSum(int[][] mat) {
        int res = 0;
        int n = mat.length;
        for (int i=0; i<n; i++) {
            res += mat[i][i];       // Primary diagonals are row = column 
            res += mat[n-1-i][i];   // Secondary diagonals are row + column = n-1!
        }
        return n % 2 == 0 ? res : res - mat[n/2][n/2]; // if n is a odd number, that mean we have added the center element twice!
    }


/* PYTHON SOLUTON VERY WEIRD APPROACH
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
*/
