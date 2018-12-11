class Solution:
    def RemoveElement(self,nums,val):
        ##判断数组是否为空
        if len(nums) !=0:
            length = len(nums)
            for i in range(length-1):
                if nums[i] == val:
                    nums.remove(nums[i])
            return len(nums)
        else:
            return 0


if __name__ == '__main__':
    Solution = Solution();
    list = [0,1,2,2,3,0,4,2]
    tmp = Solution.RemoveElement(list,2)
    print(tmp)