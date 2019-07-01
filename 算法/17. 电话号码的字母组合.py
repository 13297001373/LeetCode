class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {'2':'abc',
                 '3':'def',
                 '4':'ghi',
                 '5':'jkl',
                 '6':'mno',
                 '7':'pqrs',
                 '8':'tuv',
                 '9':'wxyz'}
        def backtrack(first,s):
            if first==length:
                res.append(s)
                return
            for item in dicts[digits[first]]:
                backtrack(first+1,s+item)

        length = len(digits)
        res = []
        if length != 0:
            backtrack(0,'')
        return res
    def letterCombinations1(self,digits):
        dp = [ '' for i in digits]
        if not digits:
            return dp
        dicts = {'2': 'abc',
                 '3': 'def',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'}
        dp[0] = [i for i in dicts[digits[0]]]
        for i,digit in enumerate(digits[1:]):
            dp[i+1] = [x+y for x in dp[i] for y in dicts[digit]]
        return dp[-1]
def test_function():
    solution = Solution()
    digits = '23'
    res = solution.letterCombinations1(digits)
    print(res)

if __name__ == '__main__':
    test_function()