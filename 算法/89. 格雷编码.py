class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # G(i) = i ^ (i/2);
        res = []
        for i in range(1<<n):
            res.append(i ^ i>>1)
        return res

def test_function():
    solution = Solution()
    n = 3
    res = solution.grayCode(n)
    print(res)

if __name__ == '__main__':
    test_function()