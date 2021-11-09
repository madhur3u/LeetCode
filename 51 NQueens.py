# https://leetcode.com/problems/n-queens/
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

# The N Queen is the problem of placing N chess queens on 
# an N×N chessboard so that no two queens attack each other.

def solveNQueens(n):

    # this will hold our answer
    ans = []

    # corner case for n == 1 ans will be [['Q]]
    if n == 1:
        return [['Q']]

    # making an n X n empty chessboard, 2d array
    chess = [['.']*n for _ in range(n)]

    # calling function which will give us our answer
    # and store the answer in ans array
    nQueensAns(n, chess, ans, 0)

    return ans

def nQueensAns(n, chess, ans, row):

    # base case
    # in the solution we are traversing in rows using recursion
    # so if we reach out of the grid we append our answer in ans array
    if row >= n:

        # making our answer
        # we need to make a 1d array with string as each row
        temp = []
        
        # traversing in each row of chess and making it string
        # temp will hold this answer
        for i in range(n):
            temp.append(''.join(chess[i]))

        # append temp to ans, return for fetching next result
        ans.append(temp)
        return

    # in each row we can only put one queen and that can be at any col
    # so loop for column and put queen once in each col and check for that
    for col in range(n):

        # this checks if we can place the queen there or not acc to question
        if checkQueen(chess, row, col):

            # if we can place the queen make that element in grid as 'Q'
            # and call the fn to put queen in next row, therefore row + 1
            chess[row][col] = 'Q'
            nQueensAns(n, chess, ans, row + 1)
            chess[row][col] = '.'

# in this we have to check if we can place the queen in the particular row and column
# for that there should be no queen above it or in any of its diagonals
# not checking below as we make grid from top to bottom
# and not checking same row as at a time we place only one queen in each row
def checkQueen(chess, row, col):

    # checking if there is a queen above in same column
    i = row - 1
    j = col
    while (i >= 0):
        if chess[i][j] == 'Q':
            return False
        i-=1

    # checking if queen in left diagonal
    i = row - 1
    j = col - 1
    while (i >= 0 and j >= 0):
        if chess[i][j] == 'Q':
            return False
        i-=1
        j-=1

    # checking if queen in right diagonal
    i = row - 1
    j = col + 1
    while (i >= 0 and j < len(chess)):
        if chess[i][j] == 'Q':
            return False
        i-=1
        j+=1
         
    # if queen was not in any of the above 3 places that means spot is valid to put queen
    return True

# _____________________main_____________________
print("Miku")
print(solveNQueens(4))
print(solveNQueens(1))
# print(solveNQueens(9))
