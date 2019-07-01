class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for k in range(len(nums)-2,-1,-1):
            if nums[k]<nums[k+1]:
                for i in range(len(nums)-1,-1):
                    if nums[i]>nums[k]:
                        nums[k], nums[i] = nums[i], nums[k]
                        break
                a = list(reversed(nums[k+1:]))
                b = nums[:k+1]
                nums = b+a
                break
        return nums


def test_function():
    solution = Solution()
    nums = [1,4,5,7,3,2,6]
    res = solution.nextPermutation(nums)
    print(res)

if __name__ == '__main__':
    test_function()

