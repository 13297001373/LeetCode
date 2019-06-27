class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)<1:
            return len(s)<1
        isOk = len(p)>=1 and (s[0]==p[0] or p[0]=='.')
        if len(p)>1 and p[1]=='*': #下一位是*，遇到*就是匹配0次或者匹配多次
            return self.isMatch(s,p[2:]) or (isOk and self.isMatch(s[1:],p))
        else: #下一位不是*
            return isOk and self.isMatch(s[1:],p[1:])


def test_function():
    solution = Solution()
    s = "aa"
    p = "a*"
    result = solution.isMatch(s,p)
    print(result)

if __name__ == '__main__':
    test_function()

