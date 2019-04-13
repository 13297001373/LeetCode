class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSubRec(nums,0,len(nums)-1)
    def maxSubRec(self,nums,start,end):
        if start==end:
            return nums[start]
        mid = (start+end)//2
        left = self.maxSubRec(nums,start,mid)
        right = self.maxSubRec(nums,mid+1,end)

        left_max = nums[mid]
        left_sum = 0
        for i in range(mid,start-1,-1):
            left_sum+=nums[i]
            if left_sum>left_max:
                left_max = left_sum

        right_max = nums[mid+1]
        right_sum = 0
        for j in range(mid+1,end+1):
            right_sum+=nums[j]
            if right_sum>right_max:
                right_max = right_sum
        return max(left,left_max+right_max,right)

def test_function():
    solution = Solution()
    nums = [1,-1,1]
    result = solution.maxSubArray(nums)
    print(result)

if __name__ == '__main__':
    test_function()
