class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while len(matrix) != 0:
            for i in range(len(matrix[0])):  # 左到右
                res.append(matrix[0].pop(0))
            del matrix[0]
            if len(matrix) == 0 or len(matrix[0])==0:
                break
            for i in range(len(matrix)):  # 上到下
                res.append(matrix[i].pop(-1))
            if len(matrix) == 0 or len(matrix[0])==0:
                break
            for i in range(len(matrix[0])):
                res.append(matrix[-1].pop(-1))  # 右到左
            del matrix[-1]
            if len(matrix) == 0 or len(matrix[0])==0:
                break
            for i in range(len(matrix)-1,-1,-1):  # 下到上
                res.append(matrix[i].pop(0))
            if len(matrix) == 0 or len(matrix[0])==0:
                break
        return res

def test_function():
    solution = Solution()
    matrix =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    res = solution.spiralOrder(matrix)
    print(res)

if __name__ == '__main__':
    test_function()


