class Solution(object):
    def generateMatrix1(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for j in range(n)] for i in range(n)] #初始化
        top = -1
        right = n
        bottom = n
        left = -1
        k = 1
        while k<n**2+1:
            for i in range(left+1,right):
                res[top+1][i] = k
                k+=1
            top+=1
            if top ==bottom:
                break

            for i in range(top+1,bottom):
                res[i][right-1] = k
                k+=1
            right -= 1
            if right==left:
                break

            for i in range(right-1,left,-1):
                res[bottom-1][i] = k
                k+=1
            bottom-=1
            if bottom == top:
                break

            for i in range(bottom-1,top,-1):
                res[i][left+1] = k
                k+=1
            left+=1
            if left==right:
                break
        return res
    def generateMatrix(self,n):
        res = [[0 for i in range(n)] for j in range(n)] #初始化
        i,j,change_i,change_j = 0,0,0,1  #赋值，初方向
        for k in range(1,n**2+1):
            res[i][j] = k
            if res[(i+change_i)%n][(j+change_j)%n]:  #遇到墙壁，改变方向
                change_i,change_j = change_j,-change_i
            i+=change_i
            j+=change_j
        return res
def test_function():
    solution = Solution()
    n = 3
    res = solution.generateMatrix(n)
    print(res)

if __name__ == '__main__':
    test_function()