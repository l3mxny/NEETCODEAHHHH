#mysolution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        #row
        m = len(matrix)
        #column
        n = len(matrix[0])
        right = m * n -1
        while left <= right:
            #binary search mid
            mid = int((left + right)/2)
            #get the (r,c) of mid 
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            #target on the right
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False