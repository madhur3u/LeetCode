# https://leetcode.com/problems/rotate-image/

def rotate(a):
	n = len(a)

	# transpose of matrix
	for i in range(n):
		for j in range (i+1,n):
			a[i][j], a[j][i] =  a[j][i], a[i][j]

	# reverse each row
	for i in range(n):
		a[i].reverse()

	

# main
matrix = [[5, 1, 9,11],
		      [2, 4,  8,10],
		      [13,3,  6, 7],
		      [15,14,12,16]]
rotate(matrix)
