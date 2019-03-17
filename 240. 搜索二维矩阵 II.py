class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        if m<1 or n<1:
            return False
        i,j =0,n-1
        while i<m and j>=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False
def test_function():
    solution = Solution()
    matrix = [[-5]]
    target = -5
    result = solution.searchMatrix(matrix,target)
    print(result)

if __name__ == '__main__':
    test_function()