class Solution:
    def LCS(self,s1,s2):
        if not s1 or not s2:
            return 0
        n1,n2 = len(s1),len(s2)
        C = [[0 for i in range(n2+1)] for j in range(n1+1)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    C[i+1][j+1] = C[i][j]+1
                else:
                    C[i+1][j+1] = max(C[i][j+1],C[i+1][j])
        return C[n1][n2]
def test_function():
    s1 = '13456778'
    s2 = '357486782'
    solution = Solution()
    result = solution.LCS(s1,s2)
    print(result)

if __name__ == '__main__':
    test_function()
