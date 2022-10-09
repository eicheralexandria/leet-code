class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        block1 = board[0][:3] + board[1][:3] + board[2][:3]
        if not self.validate(block1):
            return False
        block2 = board[0][3:6] + board[1][3:6] + board[2][3:6]
        if not self.validate(block2):
            return False
        block3 = board[0][6:] + board[1][6:] + board[2][6:]
        if not self.validate(block3):
            return False
        block4 = board[3][:3] + board[4][:3] + board[5][:3]
        if not self.validate(block4):
            return False
        block5 = board[3][3:6] + board[4][3:6] + board[5][3:6]
        if not self.validate(block5):
            return False
        block6 = board[3][6:] + board[4][6:] + board[5][6:]
        if not self.validate(block6):
            return False
        block7 = board[6][:3] + board[7][:3] + board[8][:3]
        if not self.validate(block7):
            return False
        block8 = board[6][3:6] + board[7][3:6] + board[8][3:6]
        if not self.validate(block8):
            return False
        block9 = board[6][6:] + board[7][6:] + board[8][6:]
        if not self.validate(block9):
            return False
        
            
        for row in board:
            if not self.validate(row):
                return False
        
        for i in range(9):
            col = [row[i] for row in board]
            if not self.validate(col):
                return False
        return True
        
    def validate(self, section):
        dups = []
        for sym in section:
            if sym != ".":
                num = int(sym)
                if num in dups:
                    return False
                else:
                    dups.append(num)
                if num < 1 or num > 9:
                    return False
        return True
        
sol = Solution()
board = [[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]
for row in board:
    print(row)
print(sol.isValidSudoku(board))