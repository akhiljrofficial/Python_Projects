
'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        m=len(word1)
        n=len(word2)
        res=''
        if m>=n:
            for i in range(n):
                res+=word1[i]+word2[i]
            if i!=(m-1):
                for j in range(n,m):
                    res+=word1[j]
            return res
        else:
            if m<n:
                for i in range(m):
                    res+=word1[i]+word2[i]
                for j in range(m,n):
                    res+=word2[j]
                return res
