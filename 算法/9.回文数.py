class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 0
        j = len(x)-1
        while i<j:
            if x[i]!=x[j]:
                return False
            i+=1
            j-=1
        return True

def test_fucntion():
    solution = Solution()
    x = 123432
    res = solution.isPalindrome(x)
    print(res)

if __name__ == '__main__':
    test_fucntion()