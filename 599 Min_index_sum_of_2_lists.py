# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# https://www.geeksforgeeks.org/minimum-index-sum-common-elements-two-lists/

'''
Traverse over the list1 and create an entry for index each element of list1 in a Hash Table.

Traverse over list2 and for every element, check if the same element already exists as a key in the map. 
If so, it means that the element exists in both the lists.

Find out the sum of indices corresponding to common element in the two lists. 
If this sum is lesser than the minimum sum obtained till now, update the resultant list.

If the sum is equal to the minimum sum obtained till now, put an extra entry corresponding to the element in list2 in the resultant list.
'''

import sys

list1 = ["Shogun","Tapioca Express","Burger King","KFC"] 
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

map1 = {list1[i]:i for i in range(len(list1))}          # made hashmap of 1st list, with value of list as key and index as values
ans = []                                                # this holds the ans

min_index_sum = sys.maxsize                             # we need to find minimum sum of ndex so initaite min with max value possible

for j in range(len(list2)):                             # traverse through list 2 and compare with HashMap

    if list2[j] in map1 :                               # if a element present in both lists (checking in keys of hashmap made with list2[j])
        index_sum = j + map1[list2[j]]                  # find the sum of index which will be value of dictionary and j 

        if index_sum < min_index_sum :                  # if current index sum is smaller than min_index_sum
            min_index_sum = index_sum                   # update minimum sum
            ans.clear()                                 # since we need to store only min index sum elements so clear the ans list 1st
            ans.append(list2[j])                        # and store the common element which has min sum

        elif index_sum == min_index_sum :               # if we have more elements and index sum is equal to min sum, then add that element to list also
            ans.append(list2[j])

print(ans)          


