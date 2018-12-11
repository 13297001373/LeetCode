class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        result = 0
        if n == 1:
            result = a
        if n == 2:
            result = b
        for i in range(2,n):
            result = a +b
            a = b
            b = result
        return result





if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs(4)
    print(result)