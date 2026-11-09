class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l ,r = 0, len(matrix)-1 
        while l < r:
            i = (l+r) // 2
            if matrix[i][0] > target:
                r = i - 1
            elif matrix[i][0] < target:
                l = i + 1
            else: return True
        
        if matrix[l][0] == target:  return True
        if matrix[l][0] < target: row = l
        else: row = l-1

        print(row)

        l, r = 0, len(matrix[0])-1
        print(l, r)
        while l < r:
            i = (l+r) // 2
            if matrix[row][i] > target:
                r = i - 1
            elif matrix[row][i] < target:
                l = i + 1
            else: return True
        if matrix[row][l] == target: return True

        return False