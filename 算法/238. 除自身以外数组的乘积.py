class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        forward = [1]
        for i in range(1,len(nums)):
            forward.append(forward[i-1]*nums[i-1])
        back = [1]
        for j in range(len(nums)-2,-1,-1):
            back.insert(0,back[0]*nums[j+1])
        res = []
        for i in range(len(nums)):
            res.append(forward[i]*back[i])
        return res

def test_function():
    solution = Solution()
    nums = [1]
    res = solution.productExceptSelf(nums)
    print(res)

if __name__ == '__main__':
    test_function()