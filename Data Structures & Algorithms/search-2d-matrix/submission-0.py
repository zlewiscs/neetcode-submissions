class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # % n determines which list, 
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[mid // n][mid % n] == target:
                return True
            if matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False