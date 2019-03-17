class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = 0
        for num in nums:
            n ^=num
        n &= -n  ##获取两个不同数字异或结果的最右边非1的数
        result = [0,0]
        for num in nums:
            if num&n == 0: ##把数据划分为两类
                result[0]^=num
            else:
                result[1]^=num
        return result

def test_funciton():
    nums = [1,2,1,3,2,5]
    solution = Solution()
    result = solution.singleNumber(nums)
    print(result)

if __name__ == '__main__':
    test_funciton()

