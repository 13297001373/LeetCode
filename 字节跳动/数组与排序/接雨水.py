class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #找到最大的扳子
        n = len(height)
        if n<1:
            return 0
        max_index = 0
        max_value = 0
        result = 0
        for i in range(n):
            if height[i]>max_value:
                max_value = height[i]
                max_index = i

        max_value = 0
        for i in range(max_index):
            if max_value<height[i]:
                max_value = height[i]
            else:
                result+=max_value-height[i]

        max_value = 0
        for j in range(n-1,max_index,-1):
            if max_value<height[j]:
                max_value = height[j]
            else:
                result+=max_value-height[j]
        return result


def test_function():
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solution.trap(height)
    print(result)

if __name__ == '__main__':
    test_function()


