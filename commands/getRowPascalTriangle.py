class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []
        for row in range(rowIndex+1):
            if row == 0:
                triangle.append([1])
            elif row == 1:
                triangle.append([1, 1])
            else:
                mid = self.formRow(triangle[-1])
                triangle.append([1] + mid + [1])
        return triangle[-1]
                
    def formRow(self, prevRow):
        row = []
        for i in range(len(prevRow)-1):
            row.append(prevRow[i]+prevRow[i+1])
        return row
        