class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)!=len(set(nums))

def test_function():
    solution = Solution()
    nums =[1,2,3,4,5,1]
    res = solution.containsDuplicate(nums)
    print(res)

if __name__ == '__main__':
    test_function()