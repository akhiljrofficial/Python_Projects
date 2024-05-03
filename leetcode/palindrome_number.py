"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""
class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        b=a[::-1]
        b=b.rstrip("-")
        c=int(b)
        if x==c:
            return True
        else:
            return False

s=Solution()
print(s.isPalindrome(121))