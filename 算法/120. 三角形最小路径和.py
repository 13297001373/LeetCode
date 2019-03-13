class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        result = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                result[j] = triangle[i][j] + min(result[j],result[j+1])
        return result[0]

def test_funciton():
    solution = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    result = solution.minimumTotal(triangle)
    print(result)

if __name__ == '__main__':
    test_funciton()
