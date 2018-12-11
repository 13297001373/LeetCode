class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0 :
            return 0
        opt = []
        opt.append(nums[0])
        for i in range(1,n):
            if nums[i]>opt[-1]:  ##大于的数字直接添加
                opt.append(nums[i])
            else:     ##小于的数字采用二分查找，插入nums[i]
                low = 0
                high = len(opt)-1
                mid = 0
                flag = True
                while low<high:
                    mid = (high+low)//2
                    if opt[mid] > nums[i]:
                        high = mid
                        flag = True
                    elif opt[mid] < nums[i]:
                        low = mid+1
                        flag = False
                    else:
                        opt[mid] = nums[i]
                        break
                if flag:
                    opt[mid] = nums[i]
                else:
                    opt[mid+1] = nums[i]
        return len(opt)



if __name__ == '__main__':
    solution = Solution()
    nums = [10,4,8]
    result = solution.lengthOfLIS(nums)
    print(result)