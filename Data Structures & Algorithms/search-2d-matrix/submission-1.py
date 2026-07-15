class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix)-1
        while top < bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid -1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                top = mid
                break
        #once it breaks, must point to the one we need to search in
        row = top
        left = 0 
        right = len(matrix[row]) - 1
        while left <= right:
            m = (left + right) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                right = m - 1
            else:
                left = m + 1
        return False
            

           
        