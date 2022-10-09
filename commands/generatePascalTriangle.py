class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for row in range(numRows):
            if row == 0:
                triangle.append([1])
            elif row == 1:
                triangle.append([1, 1])
            else:
                mid = self.getRow(triangle[-1])
                triangle.append([1] + mid + [1])
        return triangle
                
    def getRow(self, prevRow):
        row = []
        for i in range(len(prevRow)-1):
            row.append(prevRow[i]+prevRow[i+1])
        return row
        
        