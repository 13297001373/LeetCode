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
        lengh = len(s)
        dp = [[False if i != j else True for i in range(lengh)] for j in range(lengh)]
        best = ''
        for i in range(lengh):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):  # 只有两个字母或者前面的已经是回文
                    dp[j][i] = True
                    best = s[j:i + 1] if i - j + 1 > len(best) else best
        return best
    def Manacher(self,s):
        s = '*'.join(s)
        s = '*' + s + '*'
        p = [1 for i in s]
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            count = 0
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            p[i] += count
        max_value = max(p)
        max_index = p.index(max_value)
        print(p)
        res = ''.join(s[max_index - max_value + 1:max_index + max_value].split('*'))
        return res


def test_function():
    solution = Solution()
    s = "ccc"
    res = solution.longestPalindrome2(s)
    print(res)

if __name__ == '__main__':
    test_function()
