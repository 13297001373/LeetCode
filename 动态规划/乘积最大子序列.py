class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        minarr = []
        maxarr = []
        minarr.append(nums[0])
        maxarr.append(nums[0])
        for i in range(1,n):
            maxarr.append(max(max(maxarr[i-1]*nums[i],minarr[i-1]*nums[i]),nums[i]))
            minarr.append(min(min(maxarr[i-1]*nums[i],minarr[i-1]*nums[i]),nums[i]))
        return max(maxarr)
if __name__ =='__main__':
    solution = Solution()
    nums = [2,3,-2]
    result = solution.maxProduct(nums)
    print(result)