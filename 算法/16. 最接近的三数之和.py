class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''https://blog.csdn.net/guoziqing506/article/details/52448539'''
        if len(nums)<3:
            return 0
        nums = sorted(nums) #排序
        start = 0
        mid = start+1
        end = len(nums)-1
        min_error = 999999
        while start<end:
            while mid<end:
                sums = nums[start] + nums[mid] + nums[end]
                if abs(target-sums)<min_error:
                    min_error = abs(target-sums)
                    best_sum = sums
                if target>sums:
                    mid+=1
                elif target<sums:
                    end-=1
                else:
                    return best_sum
            start+=1
            mid = start+1
            end = len(nums)-1
        return best_sum



def test_function():
    solution = Solution()
    nums = [1,1,1,0]
    target = -100
    res = solution.threeSumClosest(nums,target)
    print(res)

if __name__ == '__main__':
    test_function()


