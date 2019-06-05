class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<-2**31 or x>2**31-1: #超出范围
            return 0
        res = []
        if x<0:
            res.append('-')
            sx = str(-x)
            i = len(sx)-1
            while i>=0:
                res.append(sx[i])
                i-=1
            return 0 if int("".join(res))<-2**31 or int("".join(res))>2**31-1 else int("".join(res))
        else:
            sx = str(x)
            i = len(sx)-1
            while i>=0:
                res.append(sx[i])
                i-=1
            return 0 if int("".join(res))<-2**31 or int("".join(res))>2**31-1 else int("".join(res))
    def reverse1(self,x):
        if x<0: #负数
            x = -x
            res = 0
            while x>0:
                res = res*10 +x%10
                x = x//10
            return 0 if -res<-2**31 else -res
        else:
            res = 0
            while x>0:
                res = res*10+x%10
                x = x//10
            return 0 if res>2**31-1 else res


def test_function():
    solution = Solution()
    x = -153
    res = solution.reverse1(x)
    print(res)

if __name__ == '__main__':
    test_function()

