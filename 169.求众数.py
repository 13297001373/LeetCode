#出现次数大于n/2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1: return None
        x = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == x:
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    x = nums[i]
                    count = 0
        count = 0
        for num in nums:
            if num == x:
                count+=1
        if count>len(nums)/2:
            return x
        else:
            return None

def test_function():
    solution = Solution()
    nums = [3,2,3]
    result = solution.majorityElement(nums)
    print(result)

if __name__ == '__main__':
    test_function()

