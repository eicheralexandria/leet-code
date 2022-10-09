class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size):
            print(matrix[size-1-i][i])
            print(matrix[i][i])
            print(matrix[size-1-i][i])
            
        
        self.display(matrix)
    def display(self, board):
        for i in board:
            print(i)
        
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(matrix)

"""
1   2   3 -> 7   4   1
4   5   6 -> 8   5   2
7   8   9 -> 9   6   3

[0][0] -> [0][2]
[0][1] -> [1][2]
[0][2] -> [2][2]

[1][0] -> [0][1]
[1][1] -> [1][1]
[1][2] -> [2][1]

[2][0] -> [0][0]
[2][1] -> [1][0]
[2][2] -> [2][0]
"""