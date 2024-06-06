class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        b=a[::-1]
        #b=b.rstrip("-")
        c=int(b)
        if x==c:
            return True
        else:
            return False

s=Solution()f
print(s.isPalindrome(121))