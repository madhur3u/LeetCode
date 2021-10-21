# https://leetcode.com/problems/non-overlapping-intervals/
# https://leetcode.com/problems/non-overlapping-intervals/discuss/91768/Python-greedy-solution-with-explanation

# Sort the intervals by their start time. [[1, 9], [2, 4], [4, 7], [6, 8], [10, 11], [10, 15], [12, 16], [20, 22]]
# If two intervals overlap, the interval with larger end time will be removed 
# so as to have as little impact on subsequent intervals as possible.

def eraseOverlapIntervals(arr):

    # sort the array by start time  
    arr.sort()
    print(arr)

    # initializing end point the end time of 1st element in sorted arr
    end = arr[0][1]
    count = 0

    print(f"{arr[0][0]}\t{arr[0][1]}\t{end}\t{count}") # debuggging and better understanding

    # linear traversal in array from 1 to n
    for s, e in arr[1:]:

        # if the current starting time is more than or equal to previous end time [12, 16], [20, 22]
        # then we don't need to merge so both can remain, dont need to remove this interval
        # since this interval is not removed the current end point will be taken so end = e
        if s >= end :
            end = e
        
        # if current st point < previous end point [1, 9], [2, 4]
        # this means it is an overlaping interval so remove this hence increase count
        # now we need to take only one of them so we take the one with lesser end time as we need to remove minimum elements
        else :
            count += 1
            end = min(end, e) # erase the one with larger end time

        print(f"{s}\t{e}\t{end}\t{count}") # debuggging and better understanding
    
    print(count) # no. of overlaping intervals to remove


# main
arr = [[6, 8], [1, 9], [2, 4], [4, 7], [10, 15], [10, 11], [12, 16], [20, 22]]
eraseOverlapIntervals(arr)
