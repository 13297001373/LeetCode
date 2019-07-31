class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        '''
        将区间的start排序，遍历区间
        区间1的end>区间2的start 
            记录相邻两区间的最大end，不用加箭
        否则
            end为区间2，要加箭
        '''
        if len(points)<1:
            return None
        points.sort(key=lambda x:x[0])
        end = points[0][1]
        res = 1
        for index in range(1,len(points)):
            if points[index][0]>end:
                res+=1
                end = points[index][1]
            else:
                end = min(end,points[index][1])
        return res
def test_function():
    solution = Solution()
    points = [[1,2],[2,4]]
    res = solution.findMinArrowShots(points)
    print(res)

if __name__ == '__main__':
    test_function()
