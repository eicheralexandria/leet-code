class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits2letter = {    
                            '2' : ['a', 'b', 'c'],
                            '3' : ['d', 'e', 'f'],
                            '4' : ['g', 'h', 'i'],
                            '5' : ['j', 'k', 'l'],
                            '6' : ['m', 'n', 'o'],
                            '7' : ['p', 'q', 'r', 's'],
                            '8' : ['t', 'u', 'v'],
                            '9' : ['w', 'x', 'y', 'z']
                        }
                        
        n = len(digits)
        if n == 0:
            return []
            
        elif n == 1:
            return digits2letter[digits[0]]
            
        elif n == 2:
            digits1 = digits2letter[digits[0]]
            digits2 = digits2letter[digits[1]]
            result = [i + j for i in digits1 for j in digits2]
            
        elif n == 3:
            digits1 = digits2letter[digits[0]]
            result = self.letterCombinations(digits[1:]) 
            result = [digit + r for digit in digits1 for r in result]
            return result
            
        elif n == 4:
            digits1 = digits2letter[digits[0]]
            result = self.letterCombinations(digits[1:]) 
            result = [digit + r for digit in digits1 for r in result]
            return result
        return result
