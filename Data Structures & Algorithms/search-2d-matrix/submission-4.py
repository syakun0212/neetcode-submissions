class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) # of rows 
        n = len(matrix[0]) # of cols 

        # Find row 
        l ,r = 0, m
        while l < r:
            mid = l + (r-l) // 2 
            if matrix[mid][n-1] > target:
                r = mid 
            elif matrix[mid][n-1] < target:
                l = mid + 1 
            else:
                return True 
        row = l 
        if row > m -1:
            return False 

        # Find col 
        l, r = 0, n 
        while l < r:
            mid = l + (r-l)//2 
            if matrix[row][mid] > target:
                r = mid 
            elif matrix[row][mid] < target:
                l = mid + 1 
            else:
                return True 
        
        return False 