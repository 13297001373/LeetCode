class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return True
        opt= nums[0]
        for i in range(1,n):
            if opt[i-1] >= i: ##判断是否可以到达i位置
                opt[i] = max(i+nums[i],opt[i-1])
            else:
                opt[i] = 0
        if opt[len(nums)-1]>=len(nums)-1:
            return True
        else:
            return False





if __name__ == '__main__':
    solution = Solution()
    nums = []
    result = solution.canJump(nums)
    print(result)