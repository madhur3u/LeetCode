// https://leetcode.com/problems/find-pivot-index/
// https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

/* Equilibrium Point in an array is a position such that the 
sum of elements before it is equal to the sum of elements after it.

approach is to consider every index, check if its a pivot point
to do this we first consider 1st index so sum towards right will be sum(a[1:]) and to left will be zero as no element present
now when we go to the next index we dont need to calculate whole sum again, we just add a[i-1] to left sum as that element now goes left to a[i]
and we will subtract a[i] from right sum, we do this till we find pivot point or loop ends

ANOTHER APPROACH --> using prefix sum we can find right and left sum for a particular index
*/
class Solution {
    public int pivotIndex(int[] a) {
        
        int n = a.length;
        int ls = 0;
        int rs = 0;
        
        for (int i = 1; i<n; i++){
            rs += a[i];
        }
        
        if (ls == rs) return 0;
        
        for (int i = 1; i<n; i++){
            ls += a[i-1];
            rs -= a[i];
            
            if (ls == rs) return i;
        }
        
        return -1;
        
    }
}
/* PYTHON SOL
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self, a, n):
        
        ls = 0
        rs = sum(a[1:])
        
        if ls == rs : return 1
        
        for i in range(1, n):
            ls += a[i - 1]
            rs -= a[i]
            
            if ls == rs : return i+1
        
        return -1 */
