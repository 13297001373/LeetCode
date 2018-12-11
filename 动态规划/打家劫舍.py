class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        opt = [nums[0],max(nums[0],nums[1])]
        for i in range(2,len(nums)):
            opt.append(max(opt[i-1],nums[i]+opt[i-2]))
        print(opt)
        return max(opt)
    def rec_rob(self,nums,n):
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])
        else:
            A = self.rec_rob(nums,n-1)
            B = self.rec_rob(nums,n-2)+nums[n-1]
            return max(A,B)



if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,4,1,7,8,3]
    result = solution.rob(nums)
    rec_result = solution.rec_rob(nums,7)
    print(result)
    print(rec_result)