class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Find correct row
        l, r = 0, m - 1
        row = -1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                row = mid
                break

        if row == -1:
            return False

        # Binary search in row
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True

        return False