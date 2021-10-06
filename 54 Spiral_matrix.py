# https://leetcode.com/problems/spiral-matrix/
# https://leetcode.com/problems/spiral-matrix/discuss/20599/Super-Simple-and-Easy-to-Understand-Solution
# see other comments

def spiral(a):

	imax = len(a) - 1
	jmax = len(a[0]) - 1
	imin = 1
	jmin = 0

	dir = 0

	i = 0
	j = 0
	c = 0

	ans = []
  
  # has to be done till count == no. of elements in matrix
	while (c < len(a) * len(a[0])):
    
    # going east first we print whole row, then increase the value of 1 when row is over
		if dir == 0:          
			ans.append(a[i][j])
			j += 1

			if j >= jmax + 1:
				jmax -= 1
				j -= 1
				i += 1
				dir = 1 
    
    # going south, will be printing the last column from 2nd element till end, decrease value of j as we printed last element here
		elif dir == 1:
			ans.append(a[i][j])
			i += 1

			if i >= imax + 1:
				imax -= 1
				i -= 1
				j -= 1
				dir = 2 
    
    # going west
		elif dir == 2:
			ans.append(a[i][j])
			j -= 1

			if j == jmin - 1:
				i -= 1
				j += 1
				jmin += 1
				dir = 3
		
    # going north
		else: # dir == 3:
			ans.append(a[i][j])
			i -= 1

			if i == imin - 1:
				j += 1
				i += 1
				imin += 1
				dir = 0

		c+=1
	
	return ans

# main
matrix = [[3,1,2],[2,3,6]]
print(*spiral(matrix))
