from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            prev_row = triangle[-1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j-1]+prev_row[j])
            row.append(1)
            triangle.append(row)
        return triangle
