class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <=1:
            return 0
        min_value = prices[0]
        max = 0
        for i in range(1,n):
            if prices[i]- max > min_value:
                max = prices[i] - min_value
            if prices[i] <min_value:
                min_value = prices[i]
        return max

if __name__ =='__main__':
    s = [7,1,5,3,6,4]
    solution  = Solution()
    s1 = solution.maxProfit(s)
    print(s1)
