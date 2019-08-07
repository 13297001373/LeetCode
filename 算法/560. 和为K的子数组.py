class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not len(nums):
            return 0
        maps = [0]
        for i in range(len(nums)):
            maps.append(maps[-1]+nums[i])
        res = 0
        for j in range(len(maps)):
            if maps[j]-k in maps[:j]:
                res+=1
        return res
def test_function():
    solution = Solution()
    nums = [0,0,0,0,0,0,0,0,0,0]
    k = 0
    res = solution.subarraySum(nums,k)
    print(res)
if __name__ == '__main__':
    test_function()