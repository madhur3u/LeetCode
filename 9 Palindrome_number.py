# https://leetcode.com/problems/palindrome-number/

# The first idea that comes to mind is to convert the number into string, 
# and check if the string is a palindrome, but this would require extra non-constant space for creating the string 

# reverse of the last half of the palindrome should be the same as the first half of the number, if the number is a palindrome.
# For example, if the input is 1221, if we can revert the last part of the number "1221" from "21" to "12", and compare it with the first half 
# of the number "12", since 12 is the same as 12, we know that the number is a palindrome.

# Now let's think about how to revert the last half of the number. For number 1221, if we do 1221 % 10, we get the last digit 1, 
# to get the second to the last digit, we need to remove the last digit from 1221, we could do so by dividing it by 10, 1221 / 10 = 122. 
# Then we can get the last digit again by doing a modulus by 10, 122 % 10 = 2, and if we multiply the last digit by 10 and add the second last digit, 
# 1 * 10 + 2 = 12, it gives us the reverted number we want. Continuing this process would give us the reverted number with more digits.

# Now the question is, how do we know that we've reached the half of the number?

# Since we divided the number by 10, and multiplied the reversed number by 10, when the original number is less than the reversed number, 
# it means we've processed half of the number digits.


def isPalindrome(x) 

        if x < 0 : return False                                   # negetive numbers are not palindrome
        if x < 10 : return True                                   # no. from 0-9 are always palindrome  
        if x % 10 == 0 : return False                             # any number with 0 in last (>=10) is not palindrome  
        
        reverse_half = 0
        while (x > reverse_half) :
            
            reverse_half = reverse_half * 10 + x % 10
            x = x // 10
            
        return (reverse_half//10 == x or reverse_half == x)       # reverse_half//10 == xis for odd cases as for odd palindrome ... (check below)
      
# main
print(isPalindrome(int(input())))

# x == rev / 10 is for odd number of digits. Suppose number is 45654, now it will come out of loop when x < rev i.e. x = 45 and rev = 456, 
# so to truncate the 6 of res, we use x = rev / 10. But this is not the case of even digits. Suppose number is 456654, 
# it will come out of loop when x <= res i.e. x = 456 and rev = 456, so no need to truncate & we can use x == rev directly for it.
