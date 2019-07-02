class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0 for i in s]
        for i in range(len(s)):
            if s[i] == ')':
                if i-1>=0 and s[i-1]=='(':
                    dp[i] = dp[i-2]+2
                if i-dp[i-1]-1>=0 and s[i-1] == ')' and s[i-dp[i-1]-1]=='(':
                    dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]
        return max(dp)
    def longestCValidParentheses1(self,s): ##暴力解法(最优的子串一定是所有正确子串的子集)
        max_count = 0
        for i in range(len(s)):
            count = 0
            for j in range(i,len(s)):
                if s[j] == '(':
                    count+=1
                else:
                    count-=1
                if count<0:
                    break
                if count==0:
                    max_count = max(max_count, j -i+1)
        return max_count
    def longestValidParentheses2(self,s):
        left = 0
        right = 0
        max_length = 0
        for item in s:
            if item == '(':
                left+=1
            else:
                right+=1
            if right>left:
                left = 0
                right = 0
            if right == left:
                max_length = max(max_length,right*2)

        left = 0
        right = 0
        for item in s[::-1]:
            if item == '(':
                left+=1
            else:
                right+=1
            if right<left:
                left = 0
                right = 0
            if right == left:
                max_length = max(max_length,right*2)
        return max_length



def test_function():
    solution = Solution()
    s = ")()())"
    dp = solution.longestValidParentheses2(s)
    print(dp)

if __name__ == '__main__':
    test_function()