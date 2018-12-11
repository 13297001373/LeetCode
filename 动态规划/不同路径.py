import datetime
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        if n == 0:
            return 0
        if m==1 or n ==1:
            return 1
        mat = [[0 for k in range(m)]for k in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j!=0:
                    mat[j][i] = 1
                if j == 0 and i!=0:
                    mat[j][i] = 1
                if i>0 and j>0:
                    mat[j][i] = mat[j-1][i]+mat[j][i-1]
        return mat[n-1][m-1]

if __name__ =='__main__':
    start = datetime.datetime.now()
    solution = Solution()
    print(solution.uniquePaths(7, 3))
    end = datetime.datetime.now()
    print('程序运行时间为：',end-start)
