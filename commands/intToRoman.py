class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral = ""
        while num != 0:
            if num >= 1000:
                numeral += "M"
                num -= 1000
            elif num >= 900:
                numeral += "CM"
                num -= 900
            elif num >= 500:
                numeral += "D"
                num -= 500
            elif num >= 400:
                numeral += "CD"
                num -= 400
            elif num >= 100:
                numeral += "C"
                num -= 100
            elif num >= 90:
                numeral += "XC"
                num -= 90
            elif num >= 50:
                numeral += "L"
                num -= 50
            elif num >= 40:
                numeral += "XL"
                num -= 40
            elif num >= 10:
                numeral += "X"
                num -= 10
            elif num >= 9:
                numeral += "IX"
                num -= 9
            elif num >= 5:
                numeral += "V"
                num -= 5
            elif num >= 4:
                numeral += "IV"
                num -= 4
            elif num >= 1:
                numeral += "I"
                num -= 1
        return numeral