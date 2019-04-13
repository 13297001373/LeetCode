class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dicts = {}
        for index in range(len(nums)):
            if nums[index] not in dicts.keys():
                dicts[nums[index]] = [1, index, index+1]
            else:
                dicts[nums[index]][0] += 1
                dicts[nums[index]][2] = index+1
        max_count = 0
        min_length = 99999
        for key in dicts:
            if dicts[key][0]>max_count:
                max_count = dicts[key][0]
                min_length = dicts[key][2]-dicts[key][1]
            if dicts[key][0]==max_count and min_length>dicts[key][2]-dicts[key][1]:
                min_length = dicts[key][2]-dicts[key][1]
        return min_length

def test_function():
    solution = Solution()
    nums = [1,2,2,3,1,4,2]
    result = solution.findShortestSubArray(nums)
    print(result)

if __name__ == '__main__':
    test_function()

