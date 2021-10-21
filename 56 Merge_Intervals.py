# https://leetcode.com/problems/merge-intervals/
# https://www.geeksforgeeks.org/merging-intervals/ 

# O(nlogn) time of sorting and O(n) extra space

# 1. Sort the intervals based on increasing order of starting time (a[i][0]).
# 2. Push the first interval on to a stack(ans)(or a list --> python lists can be used as stack).
# 3. For each interval do the following
#    a. If the current interval does not overlap with the stack top, push it.
#    b. If the current interval overlaps with stack top and ending time of current interval is more than that of stack top, 
#       update stack top with the ending  time of current interval.
# 4. At the end stack(ans) contains the merged intervals.  

def mergeIntervals(a):

    # sort the array 
    a.sort()
    print(a)
    # list ans which will have megered intervals, push 1st value of arr in it
    ans = [a[0]]

    # linear traversal in array from 1st till n 
    for i in range (1, len(a)):

        # if the 1st el of a[i] is greater than ans[-1] (last value stored in ans)
        # eg --> [5,9] in ans[-1] and [10, 13] in a[i]
        # then intervals cannot be merged so push the new interval to end
        if a[i][0] > ans[-1][1]:
            ans.append(a[i]) 

        # if [5, 9] and [9, 13] like situation occur we will merge intervals 
        # the ans[-1]'s [1] index will be changed 
        elif a[i][0] == ans[-1][1]:
            ans[-1][1] = a[i][1]
        
        # if [5, 9] and [6, 13] like situation both can be merged as the last one
        # this statement can be merged with above elif using 'or'
        elif (a[i][0] < ans[-1][1]) and (a[i][1] > ans[-1][1]):
            ans[-1][1] = a[i][1]
        
        # if whole a[i] is contained within ans[-1] --> [5,9] and [6,8] then nothing to change
        # this statement is actually not needed but written for clarity
        elif (a[i][0] < ans[-1][1]) and (a[i][1] <= ans[-1][1]):
            continue
    
    print(ans) # and will have have the merged intervals

# main
arr = [[6, 8], [1, 9], [2, 4], [4, 7], [10, 10], [10, 11], [12, 16], [20, 22]]
mergeIntervals(arr)


''' short function
for i in range (1, len(a)):

            if a[i][0] > ans[-1][1]:
                ans.append(a[i]) 
            elif (a[i][0] == ans[-1][1]) or ((a[i][0] < ans[-1][1]) and (a[i][1] > ans[-1][1])):
                ans[-1][1] = a[i][1]

            return(ans)
'''
