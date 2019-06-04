class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        s1 = len(str1)
        s2 = len(str2)
        if s1==0 or s2 ==0:
            return ""
        if s1<s2:
            smin = str1
            smax = str2
        else:
            smin = str2
            smax = str1
        for i in range(len(smin)):
            tmp = smin[i:]
            if self.check(tmp,smin) and self.check(tmp,smax):
                return tmp
        return ""
    def check(self,s,smax):
        rate = len(smax)//len(s)
        for i in range(1,rate+1):
            if s*i == smax:
                return s
        return ""

def test_function():
    solution = Solution()
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"

    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    res =  solution.gcdOfStrings(str1,str2)
    print(res)


if __name__ == '__main__':
    test_function()



