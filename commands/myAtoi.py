class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(" ")
        if s == "":
            return 0
        strNum = "0"
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        multiplier = 1
        
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            multiplier = -1
            s = s[1:]
            
        for digit in s:
            if digit in digits:
                strNum += digit
            else:
                num = int(strNum) * multiplier
                if num < ((-2)**31):
                    return ((-2)**31)
                elif num > ((2**31) - 1):
                    return ((2**31) - 1)
                return num
        
        num = int(strNum) * multiplier
        if num < ((-2)**31):
            return ((-2)**31)
        elif num > ((2**31) - 1):
            return ((2**31) - 1)
        return num