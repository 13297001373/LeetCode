class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and n&(n-1)==0

def test_function():
    solution = Solution()
    n = 16
    res = solution.isPowerOfTwo(n)
    print(res)

if __name__ == '__main__':
    test_function()
