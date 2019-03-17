class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<3: return nums
        a,b = 0,0
        ca,cb = 0,0
        for num in nums:
            if num == a:
                ca+=1
            elif num == b:
                cb+=1
            elif ca==0:
                a = num
                ca+=1
            elif cb==0:
                b = num
                cb+=1
            else:
                ca-=1
                cb-=1
        ca = 0
        cb = 0
        for num in nums:
            if num == a:
                ca+=1
            if num == b:
                cb+=1
        result = set()
        if ca>len(nums)/3:
            result.add(a)
        if cb>len(nums)/3:
            result.add(b)
        return list(result)

def test_function():
    solution =Solution()
    nums = [3,2,3]
    result = solution.majorityElement(nums)
    print(result)

if __name__ == '__main__':
    test_function()
