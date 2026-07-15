class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        cols = len(matrix[0]) - 1
        row = -1
        col = -1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][cols] >= target:
                row = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][cols] < target:
                l = mid + 1
            else:
                return False
        
        l, r = 0, cols

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                col = mid
                break
        
        return True if col != -1 else False