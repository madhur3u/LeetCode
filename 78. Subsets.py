# https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

num = [1, 2, 3, 4]                          # to find all subsets of given array
ans = []                            

for i in range(2**len(num)):                # no. of subsets = 2**n where n is no. of elements            
    x = bin(i).replace('0b','')             # find binary of the number , remove 0b 
    
    if len(x) != len(num):                  # binary for 0 is -> 0 for 1 -> 1 but we need in form of, 0000, 0001 so done this
        x = '0'*(len(num) - len(x)) + x     # modified x added 0 in front of x to make its length equal to no. of elements

    temp = []                               # this will store a subset temporarily
    
    for j in range(len(x)):                 # range will be equal to len of x, so that all value of binary compared
        
        if x[j] == '1' :                    # if we found 1 at any index, take element at that index in num and put in array
            temp.append(num[j])
    
    ans.append(temp)                        # append subset to ans

print(ans)
