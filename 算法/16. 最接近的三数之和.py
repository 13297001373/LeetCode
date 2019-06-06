class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
            return 0
        nums = sorted(nums) #排序
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i]+nums[j]<target:
                i+=1
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                break


def test_function():
    solution = Solution()
    nums = [1,2,4,8,16,32,64,128]
    target = 82
    res = solution.threeSumClosest(nums,target)
    print(res)

if __name__ == '__main__':
    test_function()


