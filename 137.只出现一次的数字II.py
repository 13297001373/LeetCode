class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b = 0,0
        for num in nums:
            a = (a^num)&~b
            b = (b^num)&~a
        return a
def test_function():
    solution = Solution()
    nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    result = solution.singleNumber(nums)
    print(result)

if __name__ == '__main__':
    test_function()

