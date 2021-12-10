# https://leetcode.com/problems/unique-paths/
# https://leetcode.com/problems/unique-paths/discuss/1582051/C%2B%2B-EASY-Intuitive-Solution-oror-Combinatorics-oror-TC-O(min(MN))-SC-O(1)-oror-Beats-100

class Solution:
    def uniquePaths(self, r: int, c: int) -> int:
        
        # we have two choices right and down
        # find total steps robot has to take tht will be r - 1 right steps and c - 1 down steps
        # so ans of steps will be like RRDDDD, RDDDDR, DDRRDD etc for 6 steps so we need to find of total comabinations of D and R
        # for that we first find what is minimum R or C so we take nCr with what we have minimum
        N = (r - 1) + (c - 1)
        R = min(r, c) - 1
        
        # program to compute nCr
        # ans will hold our answer
        # finding --> n * n-1 * n -2 .... / 1*2*3...*r in steps that is doing n/1 * n-1/2 * n-2/3 ...
        # this will be done till i reach R and we will have our answer
        ans = 1
        i = 1
        while i <= R:
            ans = (ans * N) // i
            N -= 1
            i += 1
        
        return ans
