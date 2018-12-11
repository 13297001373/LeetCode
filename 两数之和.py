# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = j = -1
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in nums and nums.index(tmp)!=i:
                j = nums.index(tmp)
                break
        if i!=-1 and j!=-1:
            return i,j
        else:
            print('error')
    def twoSum_map(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

if __name__ =='__main__':
    nums = [3,3]
    target = 6
    solution  = Solution()
    i,j = solution.twoSum(nums,target)
    print(i,j)
