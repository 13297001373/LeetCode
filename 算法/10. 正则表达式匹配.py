class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)<1:
            return len(s)<1
        isOk = len(s)>=1 and (s[0]==p[0] or p[0]=='.')
        if len(p)>1 and p[1]=='*': #下一位是*，遇到*就是匹配0次或者匹配多次
            return self.isMatch(s,p[2:]) or (isOk and self.isMatch(s[1:],p))
        else: #下一位不是*
            return isOk and self.isMatch(s[1:],p[1:])
    def isMatch1(self,s,p):
        '''
        :param s:
        :param p:
        :return:
        '''
        dp = [[True for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        for k in range(1,len(p)+1):
            if p[k-1]!='*':
                dp[k][0] = False
            else:
                dp[k][0] = dp[k-2][0]
        for k in range(1,len(s)+1):
            dp[0][k] = False
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j]!='*':
                    dp[j+1][i+1] = dp[j][i] and (p[j]=='.' or p[j]==s[i])
                else:#0次、1次、多次

        return dp[-1][-1]

def test_function():
    solution = Solution()
    s = "aab"
    p = "a*"
    result = solution.isMatch1(s,p)
    print(result)

if __name__ == '__main__':
    test_function()

