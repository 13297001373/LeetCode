class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return s

def test_function():
    solution = Solution()
    s = list('abcdefg')
    print(s)
    res = solution.reverseString(s)
    print(res)

if __name__ == '__main__':
    test_function()