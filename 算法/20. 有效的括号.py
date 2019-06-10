class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicts = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for i in s:
            try:
                if i in dicts.keys():
                    stack.append(i)
                elif i == dicts[stack[-1]]:
                    del stack[-1]
                elif i==' ':
                    continue
                else:
                    return False
            except Exception:
                return False
        return len(stack)==0

def test_function():
    solution = Solution()
    s = "(])"
    result = solution.isValid(s)
    print(result)

if __name__ == '__main__':
    test_function()
