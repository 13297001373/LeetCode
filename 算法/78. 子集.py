class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrace(first,tmp):
            if first:
                res.append(tmp)
            for i in range(first,n):
                backtrace(i+1,tmp+[nums[i]])
        n = len(nums)
        res = []
        res.append([])
        backtrace(0,[])
        return res


def test_function():
    solution = Solution()
    nums= [1,2,3]
    res = solution.subsets(nums)
    print(res)

if __name__ == '__main__':
    test_function()
