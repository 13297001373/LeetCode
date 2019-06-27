class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isHuiWen(s,left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            tmp = s[left+1:right]
            return tmp
        best = ''
        if len(s)<1:
            return best
        for i in range(len(s)):
            s1 = isHuiWen(s,i,i)
            s2= isHuiWen(s,i,i+1)
            tmp = s1 if len(s1)>len(s2) else s2
            best = tmp if len(tmp)>len(best) else best
        return best
    def longestPalindrome1(self,s):
        def isHuiWen(s,mid):
            left = mid
            right = mid
            while left>=0 and right<len(s):
                if s[left] == s[right]:
                    left-=1
                    right+=1
                else:
                    break
            return s[left+1:right].replace('*','')
        best = ''
        if len(s)<1:
            return best
        s = '*'.join(s)
        s = '*'+s+'*'
        for i in range(len(s)):
            s1 = isHuiWen(s,i)
            best = s1 if len(s1)>len(best) else best
        return best
    def longestPalindrome2(self,s):
        dp  = [[False for _ in range(len(s))] for _ in range(len(s))]
        try:
            best = s[0]
        except Exception:
            return ''
        for i in range(len(s)):
            for j in range(i):
                if s[i]==s[j] and (dp[j+1][i-1] or i-j<=2):
                    dp[j][i] = True
                    best = s[j:i+1] if len(s[j:i+1])>len(best) else best
        return best


def test_function():
    solution = Solution()
    s = "ccc"
    res = solution.longestPalindrome2(s)
    print(res)

if __name__ == '__main__':
    test_function()
