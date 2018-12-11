import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        k = 0
        for i in range(len(self.nums)):
            if nums[i] == target:
                k+=1
                if random.randint(0,len(self.nums)+1)%k:
                    return i
                #random.choice
        return None
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 2, 1, 1, 2, 3, 54, 62]
    solution = Solution(nums)
    a = solution.pick(54)
    print(a)

