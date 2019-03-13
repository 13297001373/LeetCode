class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        i = 0
        j = n-k-1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        i = n-k
        j = n-1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        i = 0
        j = n-1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        return nums

def test_function():
    solution = Solution()
    nums = [1,2,3,4,5,6]
    k = 11
    result = solution.rotate(nums,k)
    print(result)

if __name__ == '__main__':
    test_function()

