# https://leetcode.com/problems/base-7/
# Given an integer num, return a string of its base 7 representation.

def to_base7(num):

    if num == 0 : return("0")       # if number 0

    n = abs(num)                    # absolute for -ve 
    ans = ''                        # ans is a string
    while n>0:
        ans = str(n % 7) + ans      # basic base conversion adding in front of string 
        n = n // 7
    
    if num < 0 : return('-' + ans)  # if -ve value add '-' befor return
    else : return (ans)

#main
n = int(input())                    # input
print(to_base7(n))
