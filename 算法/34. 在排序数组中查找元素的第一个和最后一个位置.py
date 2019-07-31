class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''O(n)'''
        index = [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                index[0] = i if index[0]==-1 else index[0]
                index[1] = max([index[0],i])
        return index
def test_function():
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    res = solution.searchRange(nums,target)
    print(res)

if __name__ == '__main__':
    test_function()
