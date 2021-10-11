# https://leetcode.com/problems/cyclically-rotating-a-grid/

# acc to constrains, there will always be a shell

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])
        
        for shell in range(1, min(n,m)//2 + 1):		# no. of shells in a grid will be min(n,m)//2
            rotateShell(grid, shell, n, m, k)       # rotating each shell
        
        return grid
        
        
def rotateShell(arr, shell, n, m, r):

    a = make1Darray(arr, shell, n, m)
    a = rotate1Darray(a, r)
    update2darray(arr, a, shell, n, m)

# in this we make 1d array of the shell 
# same as ring rotate and return that 1d array
def make1Darray(arr, shell, n, m):

    rmin = shell - 1
    cmin = shell - 1
    rmax = n - shell
    cmax = m - shell

    a1 = []
    i = rmin
    j = cmin

    for _ in range(rmax - rmin):
        a1.append(arr[i][j])
        i+=1
    
    for _ in range(cmax - cmin):
        a1.append(arr[i][j])
        j+=1

    for _ in range(rmax - rmin):
        a1.append(arr[i][j])
        i-=1

    for _ in range(cmax - cmin):
        a1.append(arr[i][j])
        j-=1

    # print(*a1)
    return a1

# in this we rotate our 1d array and return it
def rotate1Darray(a, r):

    n = len(a)
    r = r % n
    if r == 0 : return a		# if r = 0 no need to rotate

    a = a[n - r - 1 : : -1] + a[ : n - r - 1 : -1] 
    a = a[ :: -1]
    
    return a

# in this we update our shell with the rotated 1d array in same matrix
def update2darray(arr, a1, shell, n, m):

    rmin = shell - 1
    cmin = shell - 1
    rmax = n - shell
    cmax = m - shell

    i = rmin
    j = cmin

    a1Index = 0

    for _ in range(rmax - rmin):
        arr[i][j] = a1[a1Index]
        a1Index += 1
        i+=1

    
    for _ in range(cmax - cmin):
        arr[i][j] = a1[a1Index]
        a1Index += 1
        j+=1

    for _ in range(rmax - rmin):
        arr[i][j] = a1[a1Index]
        a1Index += 1
        i-=1

    for _ in range(cmax - cmin):
        arr[i][j] = a1[a1Index]
        a1Index += 1
        j-=1

    # print(*a1)
    return a1
    
