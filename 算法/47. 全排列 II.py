class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first):
            if first == n:
                res.append(nums[:])
                return
            for i in range(first,n):
                if i>first and nums[i]==nums[i-1]:
                    continue
                nums[first],nums[i] = nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i] = nums[i],nums[first]
        n = len(nums)
        nums = sorted(nums)
        res = []
        backtrack(0)
        return res
def test_function():
    solution = Solution()
    nums = [2,2,1,1]
    res = solution.permuteUnique(nums)
    print(res)

if __name__ == '__main__':
    test_function()