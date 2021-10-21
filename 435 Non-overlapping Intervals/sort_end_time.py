# https://leetcode.com/problems/non-overlapping-intervals/
# https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling

# We can sort interval by ending time. [[2, 4], [4, 7], [6, 8], [1, 9], [10, 11], [10, 15], [12, 16], [20, 22]]
# Once next interval's start time is earlier than current end time, then we have to remove one interval. 
# Otherwise, we update earliest end time.

def eraseOverlapIntervals(arr):

    # sort the array by end time or 1th index
    # since we need to remove minimum el to make it non overlaping so we sort using 1st index  
    arr.sort(key=lambda x: x[1])
    print(arr)

    # initializing end point as -infinite
    end = float('-inf')
    count = 0

    # linear traversal in array
    for s, e in arr:

        # if the current starting time is more than or equal to previous end time [2, 4] [4, 7]
        # then we dont need to merge so both can remain, dont need to remove this interval
        # since this interval is not removed the end point of this will be taken so end = e
        if s >= end :
            end = e
        
        # if st point < previous end point [4, 7], [6, 8]
        # this means it is an overlaping interval so remove this hence increase count
        # since this one is removed so end emains unchanged 
        else :
            count += 1

        print(f"{s}\t{e}\t{end}\t{count}") # debuggging and better understanding
    
    print(count) # no. of overlaping intervals to remove


# main
arr = [[6, 8], [1, 9], [2, 4], [4, 7], [10, 15], [10, 11], [12, 16], [20, 22]]
eraseOverlapIntervals(arr)
