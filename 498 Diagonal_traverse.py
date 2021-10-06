# https://leetcode.com/problems/diagonal-traverse/
# https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING

# sum of indices in a diagonal is always equal
# loop through the matrix, store each element by the sum of its indices in a dictionary, 
# you have a collection of all elements on shared diagonals.

# The last part is easy, build your answer (a list) by elements on diagonals. 
# To capture the 'zig zag' or 'snake' phenomena of this problem, simply reverse ever other diagonal level. 
# So check if the level is divisible by 2.

n = 4
m = 6
matrix = [['00','01','02','03','04','05'],
		  [ 10,  11,  12,  13,  14,  15 ],
		  [ 20,  21,  22,  23,  24,  25 ],
		  [ 30,  31,  32,  33,  34,  35 ]]

# make a dictionary, see that sum of i + j in diagonals are always equal
# so we make dict in which key is the sum and values are a list of all diagonal elemets of that
d = {}

for i in range(n):
	for j in range(m):

		#if no entry in dictionary for sum of indices aka the diagonal, create one
		if (i+j) not in d :
			d[i+j] = [ matrix[i][j] ]

		else :
			#If you've already passed over this diagonal, keep adding elements to it!
			d[i+j].append(matrix[i][j])

# now we have all diagonals element in our dict  
ans = []

for sum in d.keys() :

	# when sum is even we need to print the value list in reverse order
	# Here we append in reverse order because its an even numbered level/diagonal 
	if sum % 2 == 0: 
		ans = ans + d[sum][::-1]
		# print(*d[sum][::-1])
	
	# otherwise print it in order
	else :
		ans = ans + d[sum]
		# print(*d[sum])

print(ans)




'''
this is the dictionary which we got with sum in index and diagonal elements corresponding to that sum in values
now we just need to print the list accordingly
when sum is even print it in reverse order and when odd print in same order

{
0: ['00'],               	reverse
1: ['01', 10], 				same
2: ['02', 11, 20],       	reverse
3: ['03', 12, 21, 30], 		same
4: ['04', 13, 22, 31], 		reverse
5: ['05', 14, 23, 32], 		same
6: [15, 24, 33], 			reverse
7: [25, 34], 				same
8: [35]						reverse
}

'''
