class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        sum = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            if sum>0:
                sum+=nums[i]
            else:
                sum = nums[i]
            result = max(result,sum)
        return result

def test_function():
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = solution.maxSubArray(nums)
    print(result)

if __name__ == '__main__':
    test_function()
