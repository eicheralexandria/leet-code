class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.runIsMatch(s, p, "")
    
    def runIsMatch(self, s, p, prev):
        
                
            
s = "ab"
p = "a*b"
sol = Solution()
print(sol.isMatch(s, p))
"""
* = zero or more of the preceding element
. = any single character
"""