class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split()
        print(tmp)
        res = []
        for item in tmp:
            res.append(''.join(list(item)[::-1]))
        return ' '.join(res)

def test_function():
    solution =Solution()
    s = "Let's it go"
    res = solution.reverseWords(s)
    print(res)

if __name__ == '__main__':
    test_function()