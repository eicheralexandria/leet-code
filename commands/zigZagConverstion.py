class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        board = [[] for i in range(numRows)]
        
        down = True
        row = 0
        for letter in s:
            if row == numRows - 1:
                down = False
            if row == 0:
                down = True
            board[row].append(letter)
            if down:
                row += 1
            else:
                row -= 1
        ret = "".join([letter for row in board for letter in row])
        return ret
