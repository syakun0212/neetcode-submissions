class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix[0])
        n = len(matrix)
        lower, upper  = 0, n-1

        while lower <= upper :
            mid = lower + (upper-lower) // 2 
            if matrix[mid][m-1] > target:
                upper = mid -1
            elif matrix[mid][m-1] < target:
                lower = mid +1 
            else: 
                return True 
        row = lower

        if row == n:
            return False 

  
        l, r = 0, m-1
        while l <= r:
            mid = l + (r-l) // 2 
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1 
            else: 
                return True 

        return False 


