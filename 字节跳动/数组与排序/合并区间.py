# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        result = []
        for interval in intervals:
            if not result or result[-1].end <interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end,interval.end)
        return result
def test_function():
    a = Interval(1,3)
    b = Interval(2,6)
    c = Interval(15,18)
    d = Interval(8,10)
    intervals = [a,b,c,d]
    solution = Solution()
    result = solution.merge(intervals)
    for i in result:
        print(i.start,i.end)


if __name__ == '__main__':
    test_function()

