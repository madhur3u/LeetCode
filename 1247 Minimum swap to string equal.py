# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

def strswap(s1,s2):

    # s1 = 'xx'
    # s2 = 'xy'

    # p1 is no. of x y unmatched pairs
    # p2 is no. of y x unmatched pairs
    # unp is no.of unmatched pairs
    p1, p2, unp = 0, 0, 0

    for i in range(len(s1)):

        # if pair is unmatched we increment pi, p2 and unp
        if s1[i] != s2[i]:

            unp += 1
            if s1[i] == 'x' and s2[i] == 'y' : p1 += 1
            else : p2 += 1

    # if we have odd no. of unmatched pairs then
    # we can never get same after swap so return -1
    if unp % 2 != 0 : 
            return -1

    else: 
        
        # if pairs are even they can be swapped like 2 pairs with 1 swap
        # so ans is unp / 2
        if p1 % 2 == 0 and p2 % 2 == 0 :
            return unp // 2

        # but if it is odd, we will have one pair like x | y and y | x left
        # this last pair will take 2 swap rest all pairs can be matched 
        else :
            return (unp - 2)//2 + 2

# main code
s1 = 'xxyyxyxyxx'
s2 = 'xyyxyxxxyx'

print(strswap(s1, s2))
