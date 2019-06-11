class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrace(first,tmp):
            if tmp not in res:
                res.append(tmp)
            for i in range(first,n):
                backtrace(i+1,tmp+[nums[i]])
        n = len(nums)
        nums = sorted(nums)
        res = []
        res.append([])
        backtrace(0,[])
        return res

def test_function():
    solution = Solution()
    nums= [4,4,4,1,4]
    res = solution.subsetsWithDup(nums)
    print(res)

if __name__ == '__main__':
    test_function()
