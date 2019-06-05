class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = ['0','1','2','3','4','5','6','7','8','9']
        res = []
        isNum = False
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        for s in str:
            if (s =='+' or s=='-') and not isNum:
                res.append(s)
                isNum = True
            elif s in nums:
                res.append(s)
                isNum = True
            elif s == ' ' and not isNum:
                continue
            else:
                break
        print(res)
        res = ''.join(res)
        try:
            res = int(res)
        except Exception:
            res = 0
        if res>INT_MAX:
            return INT_MAX
        elif res<INT_MIN:
            return INT_MIN
        else:
            return res

def testfunction():
    solution = Solution()
    str  = '+0 123'
    res = solution.myAtoi(str)
    print(res)

if __name__ == '__main__':
    testfunction()



