import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            if first==n:
                res.append(nums[:])
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i] = nums[i],nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res
def test_function():
    solution = Solution()
    nums = [1,2]
    res = solution.permute(nums)
    print(res)


if __name__ == '__main__':
    test_function()

