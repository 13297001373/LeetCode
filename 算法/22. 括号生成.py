class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrace(left,right,s):
            if right>left or left>n:
                return
            if right==n:
                res.append(s)
                return
            backtrace(left+1,right,s+'(')
            backtrace(left,right+1,s+')')
        res = []
        backtrace(0,0,'')
        return res

def test_function():
    solution = Solution()
    res = solution.generateParenthesis(4)
    print(res)

if __name__ == '__main__':
    test_function()