class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #每一个人最优的选择
        return n%4!=0
def test_function():
    solution = Solution()
    n = 1348820612
    res = solution.canWinNim(n)
    print(res)

if __name__ == '__main__':
    test_function()

