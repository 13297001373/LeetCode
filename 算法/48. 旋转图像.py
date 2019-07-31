class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        arr = matrix.copy()
        for i in range(len(matrix)):
            matrix[i] = [arr[j][i] for j in range(len(matrix)-1,-1,-1)]
        return matrix

def test_function():
    solution = Solution()
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    res = solution.rotate(matrix)
    print(res)

if __name__ == '__main__':
    test_function()