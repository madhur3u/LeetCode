# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def product_sum_diff(num):

    p = 1
    s = 0

    for i in range(len(str(num))):

        p = p * int(str(num)[i])
        s = s + int(str(num)[i])
    
    return (p-s)
        

#main
n = int(input())
print(product_sum_diff(n))
