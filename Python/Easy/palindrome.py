#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        return x == reverted or x == reverted // 10


    ''''
    Logic:

    Negative numbers and numbers ending in 0 (except 0 itself) can't be palindromes — return False immediately.

    Reverse only the second half of the number by repeatedly peeling off the last digit of x and appending it 
    to reverted, stopping once x <= reverted (the midpoint).

    For even-length numbers, x == reverted. For odd-length numbers, the middle digit sits in reverted, so drop it 
    with reverted // 10 before comparing.

    '''