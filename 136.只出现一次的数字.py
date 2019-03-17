'''
异或运算：相同数字异或之后为0，数字和0异或为数字
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result^=num
        return result

def test_function():
    solution = Solution()
    nums = [2,2,1,1,3]
    result = solution.singleNumber(nums)
    print(result)

if __name__ == '__main__':
    test_function()