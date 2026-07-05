class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target:
                top = mid + 1
            else:
                bottom = mid - 1
        if bottom < 0:
             return False
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[bottom][middle] == target:
                return True
            if matrix[bottom][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False