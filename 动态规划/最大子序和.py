class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n ==0 :
            return 0
        result = nums[0]
        tmp = result
        for i in range(1,n):
            if tmp+nums[i] >nums[i]:
                tmp+=nums[i]
            else:
                tmp = nums[i]
            if tmp > result:
                result = tmp
        return result
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    result = solution.maxSubArray(nums)
    print(result)