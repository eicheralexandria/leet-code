class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        print("len_s:", len_s)
        if len_s == 1:
            return s
        for i in range(len_s-1, -1, -1):
            print(i)
        
        

        
sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))

"""
len-4                len-3                len-2                len-1                    len-0  
b = s[0:len-4]       ba = s[0:len-3]      bab = s[0:len-2]     baba = s[0:len-1]        babad = s[0:len]
a = s[1:len-3]       ab = s[1:len-2]      aba = s[1:len-1]     abad = s[1:len]
b = s[2:len-2]       ba = s[2:len-1]      bad = s[2:len]
a = s[3:len-1]       ad = s[3:len]
d = s[4:len] 

"""

        