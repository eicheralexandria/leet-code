class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        romanToInt = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        len_s = len(s)
        i = 0
        while i < len_s:
            numeral = s[i]
            if numeral == "I":
                if i + 1 < len_s:
                    nextNumeral = s[i+1]
                    if nextNumeral == "V":
                        num += 4
                        i += 2
                    elif nextNumeral == "X":
                        num += 9
                        i += 2
                    else:
                        num += 1
                        i += 1
                else:
                    num += 1
                    i += 1
            if numeral == "V":
                num += 5
                i += 1
            elif numeral == "X":
                if i + 1 < len_s:
                    nextNumeral = s[i+1]
                    if nextNumeral == "L":
                        num += 40
                        i += 2
                    elif nextNumeral == "C":
                        num += 90
                        i += 2
                    else:
                        num += 10
                        i += 1
                else:
                    num += 10
                    i += 1
            elif numeral == "L":
                num += 50
                i += 1
            elif numeral == "C":
                if i + 1 < len_s:
                    nextNumeral = s[i+1]
                    if nextNumeral == "D":
                        num += 400
                        i += 2
                    elif nextNumeral == "M":
                        num += 900
                        i += 2
                    else:
                        num += 100
                        i += 1
                else:
                    num += 100
                    i += 1
            elif numeral == "D":
                num += 500
                i += 1
            elif numeral == "M":
                num += 1000
                i += 1
                
        return num