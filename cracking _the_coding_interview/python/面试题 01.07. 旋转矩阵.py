class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return

        k, size = 1, len(matrix)

        while size >= 2 * k:
            top = left = k - 1
            bottom = right = size - k
            for i in range(right - left):
                tmp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = tmp
            k += 1
        
        return