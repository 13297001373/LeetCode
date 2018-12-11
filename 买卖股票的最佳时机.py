'''
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
'''
class Solution:
    def maxProfit(self, prices):
        '''
        :param prices:
        :return:
        '''
        max_price = 0
        length = len(prices)
        if length == 0:
            return 0
        else:
            i = 0
            while i < length:
                j = i+1
                while j <length:
                    if prices[j]>prices[i]:
                        temp = prices[j]-prices[i]+self.maxProfit(prices[(j+1):])
                        if temp>max_price:
                            max_price = temp
                    j+=1
                i+=1
            return max_price
    def maxprofit(self,prices):
        '''

        :param prices:
        :return:
        '''
        result = 0
        buy = 9999
        for price in prices:
            buy = min(buy,price)
            result = max(result,price-buy)
        return result





if __name__ == '__main__':
    solution = Solution()
    list = [7,1,5,3,6,4]
    value = solution.maxProfit(list)
    print(value)